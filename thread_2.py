import time
import tracemalloc
import logging
import requests
import threading

def fetch_url(url):
    try:
        response = requests.get(url)
    except Exception as e:
        logging.info(f'Could not fetch {url}. Error {e}.')
    return response.content

def fetch_all(url_list):
    threads = list()
    for link in url_list:
        thread = threading.Thread(target=fetch_url, args=(link,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    
        

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    test_url = 'https://www.google.com/'
    tracemalloc.start()

    for ntimes in [1, 10, 100, 500]:
        start = time.time()
        responses = fetch_all([test_url] * ntimes)
        logging.info(f'Fetch {ntimes} url for {time.time() - start} seconds.')

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
