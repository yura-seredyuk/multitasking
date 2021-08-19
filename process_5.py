import time
import tracemalloc
from multiprocessing import Pool



def single_function_write(index):
    with open(f'files/read/file_{index+1}_read.txt', 'r') as f:
        info = f.read()
        # f.write(f'Read text {index+1}')

    with open(f'files/write/file_{index+1}_write.txt', 'w') as f:
        f.write(info)


def pool_handler():
    p = Pool()
    p.map(single_function_write, range(10000))

if __name__ == "__main__":
    tracemalloc.start()
    start = time.time()

    pool_handler()

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))
