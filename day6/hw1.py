import threading
import time
import queue
import random
from typing import *

q = queue.Queue()
balance = 1000.00

def producer(q: queue.Queue, amount: float, transaction_type: str, t_id: int):
    q.put((transaction_type, amount))
    print(f"\033[95mProducer {t_id}\033[0m, {transaction_type} amount: {amount}")
    
def consumer(q: queue.Queue, c_id: int):
    global balance
    while True:
        task = q.get()
        if task is None:
            q.task_done()
            print(f"\033[92mConsumer-{c_id}\033[0m completed transaction. Exiting...")
            break
        
        transaction_type, amount = task 
        if transaction_type == "withdraw":
            if balance >= amount:            
                balance -= amount
            else:
                print(f"\033[91mFailed withdrawal of {amount:.2f}, balance too low\033[0m")
                
        elif transaction_type == "deposit":
            balance += amount
        else:
            q.task_done()
            print(f"Unknown transaction. Exiting....")
            break
        print(f"\033[94mConsumer-{c_id}\033[0m performed {transaction_type} operation. Updated amount: {balance}")
            
        # time.sleep(random.random())
        time.sleep(.2)
        q.task_done()     # Transaction has processed


# Multiple consumers
consumers = []
for i in range(2):
    consumer_thread = threading.Thread(target=consumer, args=(q, i))
    consumer_thread.start()
    consumers.append(consumer_thread)    

# Multiple producers
producers = []
def multi_thread_producers():
    for i in range(0,10):
        new_amt = random.random() * random.randint(1,1000)
        task = ""
        if random.random() > 0.5:
            task = "deposit"
        else:
            task = "withdraw"
        producer_thread = threading.Thread(target=producer, args=(q, new_amt, task, i))
        time.sleep(random.random())
        producers.append(producer_thread)
        producer_thread.start()

    for _ in range(len(consumers)):
        q.put(None)

multi_thread_producers()

# Join all producers
for p in producers:
    p.join()

# Join all consumers
for c in consumers:
    c.join()


# Join the queue
q.join()

print("Finished all bank transactions. Final balance:",balance)
