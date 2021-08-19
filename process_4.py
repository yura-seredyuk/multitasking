from data_dict import data
import time
import tracemalloc
from multiprocessing import Pool

def clear_file():
    with open('test_4.txt', 'w') as f:
        f.close()

def single_function(DATA):
    with open('test_4.txt', 'a') as f:
        for i in range(DATA[1]*10000):
            f.write(DATA[0])

def pool_handler():
    p = Pool()
    p.map(single_function, data)


if __name__ == '__main__':
    clear_file()
    tracemalloc.start()
    start = time.time()

    pool_handler()

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))
