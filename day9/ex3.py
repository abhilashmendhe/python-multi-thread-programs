# Example 2: Producer waits for Consumer

import threading 
import time 
import random 

condition = threading.Condition()
data_ready = False 


def consumer():
    global data_ready
    with condition:
        print("Consumer waiting for data...")
        while not data_ready:
            condition.wait()
        print("Consumer got the data....")

def producer():
    global data_ready
    print("Producer generating data....")
    time.sleep(random.randint(1,5))
    with condition:
        data_ready = True
        print("Producer has the data. Notifying consumer...")
        condition.notify()

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()

t1.join()
t2.join()