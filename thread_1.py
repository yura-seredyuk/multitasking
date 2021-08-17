from data_dict import data
import time
import tracemalloc
import logging
import threading

def single_function(name, delay):
    logging.info(f'Task {name} started.')
    time.sleep(delay)
    logging.info(f'Task {name} finished.')

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

threads = []
tracemalloc.start()
start = time.time()
for item in data:
    thread = threading.Thread(target=single_function, args=(item[0], item[1],),)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
