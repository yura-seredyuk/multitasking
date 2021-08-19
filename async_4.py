from data_dict import data
import time
import tracemalloc
import asyncio
import itertools 
import aiofiles

def clear_file():
    with open('test_4.txt', 'w') as f:
        f.close()

async def single_function(text, count):
    async with aiofiles.open('test_4.txt', 'a') as f:
        for i in range(count*10000):
            await f.write(text)

# clear_file()

tracemalloc.start()
start = time.time()
loop = asyncio.get_event_loop()
tasks = itertools.starmap(single_function, data)
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
