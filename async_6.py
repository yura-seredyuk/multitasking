import time
import tracemalloc
import asyncio
import aiofiles
import aiohttp


def clear_file():
    with open('to_do_file.txt', 'w') as f:
        f.close()

sum = 0
async def single_function(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://jsonplaceholder.typicode.com/todos/{id}') as response:
            data = await response.json()
            print(data)
            global sum 
            sum += 1
    asyncio.sleep(1)
    async with aiofiles.open('to_do_file.txt', 'a') as f:
        await f.write(f'id:{data["id"]} userId:{data["userId"]} title:{data["title"]} completed:{data["completed"]}\n')

async def main():
    tasks = [asyncio.create_task(single_function(i)) for i in range(1,201)]
    await asyncio.gather(*tasks)

clear_file()
loop = asyncio.get_event_loop()
tracemalloc.start()
start = time.time()

asyncio.run(main())
loop.close()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
print(f'SUMM {sum}')