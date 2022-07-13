'''Accessing the event loop'''

import asyncio
from prince.delay_functions_prince import delay

def call_later():
    print("I'm being called in the future")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(5)

asyncio.run(main())