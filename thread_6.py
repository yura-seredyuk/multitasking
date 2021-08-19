import time
import tracemalloc
import requests
import threading


def clear_file():
    with open('to_do_file.txt', 'w') as f:
        f.close()

def single_function(id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id}')
    data = response.json()

    with open('to_do_file.txt', 'a') as f:
        f.write(f'id:{data["id"]} userId:{data["userId"]} title:{data["title"]} completed:{data["completed"]}\n')

clear_file()
threads = []
tracemalloc.start()
start = time.time()
for item in range(1,201):
    thread = threading.Thread(target=single_function, args=(item,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()    

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
