import asyncio
import requests
import sys
sys.path.append('/Users/apple/Desktop/async_python/')

from util.timer import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get("https://www.example.com").status_code

@async_timed()
async def main():
    task_one = asyncio.create_task(get_example_status())
    task_two = asyncio.create_task(get_example_status())
    await task_one
    await task_two

asyncio.run(main())

