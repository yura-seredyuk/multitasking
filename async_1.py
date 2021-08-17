from asyncio import tasks
from data_dict import data
import time
import tracemalloc
import logging
import asyncio
import itertools

loop = asyncio.get_event_loop()

async def single_function(name, delay):
    logging.info(f'Task {name} started.')
    await asyncio.sleep(delay)
    logging.info(f'Task {name} finished.')

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

tracemalloc.start()
start = time.time()

responses = itertools.starmap(single_function, data)
loop.run_until_complete(asyncio.gather(*responses))
loop.close()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
