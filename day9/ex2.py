# 2. Thread events with 2 worker threads

import threading
import time 
import random 

event = threading.Event()

def worker(i):
    
    print(f"Worker {i} - Starting worker, Waiting for event....")
    event.wait()
    print(f"Worker {i} - Received signal, will start to work now")
    ts = random.randint(3,8)
    print(f"Worker {i} is sleeping for {ts} seconds.")    
    time.sleep(ts)
    print(f"Worker {i} finished work....")
    
threads = []
for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)
    

print("Main: Sleeping for 3 seconds...")
time.sleep(3)

print("Main: Sending signal")
event.set()

for t in threads:
    t.join()
    
print("Main: All done")