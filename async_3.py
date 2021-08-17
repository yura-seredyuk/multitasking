import time
import tracemalloc
import asyncio

async def single_function(x):
    return x ** x

async def main():
    tasks = [asyncio.create_task(single_function(i)) for i in range(1000000, 1000016)]
    await asyncio.gather(*tasks)

tracemalloc.start()
start = time.time()

asyncio.run(main())

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
