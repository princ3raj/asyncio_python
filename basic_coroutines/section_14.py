import asyncio
import time

async def main():
    start = time.time()
    await asyncio.sleep(1)
    end = time.time()

    print(f"sleeping took {end-start} seconds")

asyncio.run(main())


