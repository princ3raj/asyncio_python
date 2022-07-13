from asynchat import async_chat
import asyncio

async def hello_world_message() -> str:
    await asyncio.sleep(10)
    print("hello world")

async def main() -> None:
    message = await hello_world_message()
    print(message)

asyncio.run(main())
