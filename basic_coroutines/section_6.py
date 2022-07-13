import asyncio
from prince.delay_functions_prince import delay


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) is {fib(number)}')

async def main():
    sleep_for_three = asyncio.create_task(delay(1))
    print(type(sleep_for_three))
    print_fib(25)
    result = await sleep_for_three
    print(result)

asyncio.run(main())