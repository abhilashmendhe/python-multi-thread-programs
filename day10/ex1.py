"""
    Day 10: Learning semaphore
"""
import threading
import time 
import random

sema = threading.Semaphore(3)

def fun(ind):
    print(f"Thread {ind} is waiting...")
    with sema:
        print(f"Thread-{ind} got a lock")
        time.sleep(random.uniform(1,4))
        print(f"Thread-{ind} released lock")
        
threads = []
for i in range(5):
    t = threading.Thread(target=fun, args=(f"{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
print("Completed...")