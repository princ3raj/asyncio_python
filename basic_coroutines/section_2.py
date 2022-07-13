import asyncio

async def couroutine_add(number: int) -> None:
    return number + 1

def add_number(number: int) -> None:
    return number + 1

func_result = add_number(234)
couroutine_result = asyncio.run( couroutine_add(234))

print(f"result is {func_result} and the type is {type(func_result)}")
print(f"result is {couroutine_result} and the type is {type(couroutine_result)}")
