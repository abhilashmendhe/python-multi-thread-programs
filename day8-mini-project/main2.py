import requests
import threading
import queue
import sys

def producer(q: queue.Queue, start, end):
    q.put((start, end))
    print(f"\033[91mProducer\033[0m sending chunks indices start: {start} - end: {end}")

def consumer(q: queue.Queue, URL, file_name):
    while True:
        indices = q.get()
        if indices is None:
            q.task_done()
            print(f"\033[93mConsumer\033[0m exiting... Fetched all the video chunks")
            break
        start, end = indices
        print(f"\033[94mConsumer\033[0m fetching chunks: {indices}")
        chunk_downloader(start, end, URL, file_name)
        q.task_done()

def chunk_downloader(start, end, url, file_name):
    headers = {'Range':f'bytes={start}-{end}'}
    r = requests.get(url, headers=headers, stream=True)

    with open(file_name, "r+b") as fp:
        fp.seek(start)
        fp.write(r.content)


if __name__ == '__main__':
    
    args = sys.argv
    
    if len(args) < 2:
        print("First argument should be a URL")
        exit(1)
    
    URL = args[1]
    
    if len(args) < 3:
        print("Second argument should be a file name")
        exit(1)
        
    file_name = args[2]
    
    if len(args) < 3:
        print("Third argument should be the number of threads")
        exit(1)
    
    num_threads = int(args[3])
    
    r = requests.get(URL)
    
    download_q = queue.Queue()

    if r.status_code == 200:
        try:
            file_size = int(r.headers['Content-Length'])
        except:
            print("Missing Content-Length header. Can't download the file..")
            exit(1)
        
        print(f"File size: {file_size}")
        with open(file_name, "wb") as fp:
            fp.write(b'\0'*file_size)
        
        consu_threads = []
        for c in range(4):
            consu_t = threading.Thread(target=consumer, args=(download_q, URL, file_name))
            consu_t.start()
            consu_threads.append(consu_t)
        
        file_chunks = file_size // num_threads
        prod_threads = []
        def start_multi_thread_prod():
            for i in range(num_threads):
                start = file_chunks * i
                end = file_size - 1 if i == num_threads - 1 else (start + file_chunks - 1)
                prod = threading.Thread(target=producer, args=(download_q, start, end))
                prod_threads.append(prod)
                prod.start()
            # download_q.put(None)
            for _ in range(len(consu_threads)):
                download_q.put(None)

        start_multi_thread_prod()
        for prod in prod_threads:
            prod.join()

        # consumer_thread.join()
        for c in consu_threads:
            c.join()
            
        download_q.join()
        
        print(f'{file_name} downloaded successfully!')
        
    else:
        print(f"Invalid request: {r.status_code}")
        exit(1)


"""
$ python main.py https://thetestdata.com/assets/video/mp4/highquality/5k_Thetestdata.mp4 movie.mp4 4
"""
    