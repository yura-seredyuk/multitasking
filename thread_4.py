from data_dict import data
import time
import tracemalloc
import threading

def clear_file():
    with open('test_4.txt', 'w') as f:
        f.close()

def single_function(text, count):
    with open('test_4.txt', 'a') as f:
        for i in range(count*10000):
            f.write(text)

clear_file()
threads = []
tracemalloc.start()
start = time.time()
for item in data:
    thread = threading.Thread(target=single_function, args=(item[0], item[1], ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
