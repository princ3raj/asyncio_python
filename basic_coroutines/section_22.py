'''Changing the slow callback duration'''

import asyncio
async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .00000000250

asyncio.run(main(),debug= True)