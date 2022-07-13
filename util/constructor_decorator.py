import inspect
from dataclasses import dataclass
from functools import wraps
import functools
from inspect import Parameter, signature
import itertools

# sig = inspect.signature(func);
# bound = sig.bind(*args, **kwargs);
# for param in sig.parameters.values():
#       setattr(selfobj, param.name, bound.get(param.name, param.default))
def instanceVariables(func):
    def returnFunc(*args, **kwargs):
        selfVar = args[0]

        argSpec = inspect.getargspec(func)
        argumentNames = argSpec[0][1:]
        defaults = argSpec[3]
        if defaults is not None:
            defaultArgDict = dict(zip(reversed(argumentNames), reversed(defaults)))
            selfVar.__dict__.update(defaultArgDict)

        argDict = dict(zip(argumentNames, args[1:]))
        selfVar.__dict__.update(argDict)

        validKeywords = set(kwargs) & set(argumentNames)
        kwargDict = {k: kwargs[k] for k in validKeywords}
        selfVar.__dict__.update(kwargDict)

        func(*args, **kwargs)

    return returnFunc

class Test():

    @instanceVariables
    def __init__(self, x, y=100, z=200):
        pass

    def printStr(self):
        print(self.x, self.y, self.z)



@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

inventoryItem =InventoryItem("prince",12.2,2)
print(inventoryItem.total_cost())


def instance_variables(f):
    sig = signature(f)
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        values = sig.bind(self, *args, **kwargs)
        for k, p in sig.parameters.items():
            if k != 'self':
                if k in values.arguments:
                    val = values.arguments[k]
                    if p.kind in (Parameter.POSITIONAL_OR_KEYWORD, Parameter.KEYWORD_ONLY):
                        setattr(self, k, val)
                    elif p.kind == Parameter.VAR_KEYWORD:
                        for k, v in values.arguments[k].items():
                            setattr(self, k, v) 
                else:
                    setattr(self, k, p.default) 
    return wrapper

class Point(object):
    @instance_variables 
    def __init__(self, x, y, z=1, *, m='meh', **kwargs):
        pass


def autoinit(func):
    """
    This decorator function auto initialize class variables from __init__() arguments
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ != '__init__':
            return func(*args, **kwargs)

        self = args[0]
        func_spec = inspect.getfullargspec(func)

        # initialize default values
        nargs = dict()
        if func_spec.kwonlydefaults is not None:
            for k,v in func_spec.kwonlydefaults.items():
                nargs[k] = v
        if func_spec.defaults is not None:
            for k,v in zip(reversed(func_spec.args), reversed(func_spec.defaults)):
                nargs[k] = v
        if func_spec.varargs is not None:
            nargs[func_spec.varargs] = []
        if func_spec.varkw is not None:
            nargs[func_spec.varkw] = {}
        # fill in positional arguments
        for index, v in enumerate(args[1:]):
            if index+1 < len(func_spec.args):
                nargs[func_spec.args[index+1]] = v
            elif func_spec.varargs is not None:
                # variable argument
                nargs[func_spec.varargs].append(v)
        # fill in keyword arguments
        for k,v in kwargs.items():
            if k in itertools.chain(func_spec.args, func_spec.kwonlyargs):
                nargs[k] = v
            elif func_spec.varkw is not None:
                # variable keywords
                nargs[func_spec.varkw][k] = v

        # set values to instance attributes
        for k,v in nargs.items():
            setattr(self, k, v)
        return func(*args, **kwargs)
    return wrapper