'''Running CPU bound code in debug mode'''

import asyncio
from prince.prince_timer import async_timed

@async_timed()
async def cpu_bound_work():
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter

async def main():
    task_one =  asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(), debug= True)
