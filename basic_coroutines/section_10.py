import asyncio
from prince.delay_functions_prince import delay

async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task,timeout=1)
        print(result)
    except:
        print('Got a timeout')
        print(f'was the task cancelled ?, {delay_task.cancelled()}')

asyncio.run(main())