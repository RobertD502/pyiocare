import asyncio
import time
from itertools import islice
from aiohttp import ClientSession
from pyiocare.coway_client import CowayClient


async def main() -> None:
    async with ClientSession() as session:
        client = CowayClient('email', 'password', session)
        await client.login()
        data = await client.async_get_purifiers_data()

start_time = time.time()
asyncio.get_event_loop().run_until_complete(main())
print("--- %s seconds ---" % (time.time() - start_time))
