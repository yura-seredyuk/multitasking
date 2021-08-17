import time
import tracemalloc
import logging
import asyncio
from aiohttp import ClientResponseError, ClientSession
from requests.sessions import session

async def fetch_url(session, url):
    try:
       async with session.get(url, timeout=15) as response:
           resp = await response.read()
           print(response.status_code)
    except ClientResponseError as e:
        logging.warning(e.code)
    except asyncio.TimeoutError as e:
        logging.warning("Timeout!")
    except Exception as e:
        logging.warning(e)
    else:
        return resp
    return

async def fetch_all(loop, count):
    test_url = 'https://www.google.com/'
    tasks = []
    async with ClientSession() as session:
        for i in range(count):
            task = asyncio.ensure_future(fetch_url(session, test_url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    tracemalloc.start()

    for ntimes in [10]:
        start = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_all(loop, ntimes))
        loop.run_until_complete(future)
        responses = future.result()
        logging.info(f'Fetch {ntimes} url for {time.time() - start} seconds.')

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
