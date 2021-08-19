import time
import tracemalloc
import asyncio
import aiofiles


async def single_function_write(index):
    async with aiofiles.open(f'files/read/file_{index+1}_read.txt', 'r') as f:
        info = await f.read()
        # f.write(f'Read text {index+1}')

    async with aiofiles.open(f'files/write/file_{index+1}_write.txt', 'w') as f:
        await f.write(info)

async def main():
    tasks = [asyncio.create_task(single_function_write(i)) for i in range(8190)]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
tracemalloc.start()
start = time.time()

asyncio.run(main())
loop.close()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
