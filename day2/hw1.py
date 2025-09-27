import threading 
from time import sleep

print("Main started......")

def worker(n):
    print(f"I am thread: {n}. My name is {threading.current_thread().name}")
    sleep(.5)    

threads = []
for i in range(1,11):
    t = threading.Thread(target=worker, name=f"Worker - {i}", args=(i,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
print("Main thread finished")