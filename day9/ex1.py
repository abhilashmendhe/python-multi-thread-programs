# 1. Thread events

import threading 
import time  


event = threading.Event()

def worker():
    print("Worker: Waiting for the signal...")
    event.wait()
    print("Worker: received signal! starting work")
    time.sleep(5)
    print("Worker: Finished the task...")
    
t = threading.Thread(target=worker)
t.start()

print("Main: Sleeping for 3 seconds...")
time.sleep(3)


print("Main: Sending signal")
event.set()

t.join()
print("Main: All done")