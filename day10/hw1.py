"""
    HW: Only 3 printers and 10 users.
"""

import threading
import time 
import random

sema = threading.Semaphore(3)

def printer(user: str):
    print(f"Printer receieved request from {user}")
    with sema:
        print(f"Printing for {user}")
        time.sleep(random.uniform(1,4))
        print(f"Printed for {user}")

threads = []
for i in range(5):
    t = threading.Thread(target=printer, args=(f"User-{i}",))
    threads.append(t)
    t.start()    

for t in threads:
    t.join()
    
print("Complted all jobs by printer...")