import time
import tracemalloc


def single_function_write(index):
    with open(f'files/read/file_{index+1}_read.txt', 'r') as f:
        info = f.read()
        # f.write(f'Read text {index+1}')

    with open(f'files/write/file_{index+1}_write.txt', 'w') as f:
        f.write(info)

tracemalloc.start()
start = time.time()
for i in range(10000):
    single_function_write(i)

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
