import asyncio
from unittest import result
from prince.delay_functions_prince import delay

async def main():
    task = asyncio.create_task(delay(20))

    try:
        result = await asyncio.wait_for(asyncio.shield(task),5)
        print(result)
    except:
        print("Task took longer than five seconds, it will finish soon!")
        result = await task
        print(result)

asyncio.run(main())