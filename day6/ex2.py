# 2. Multi producer and single consumer

import queue
import threading
import time
import random

def producer(q,i):
    item = f"Data-{i}"
    q.put(item)
    print(f"\033[91mProducer\033[0m put: {item}")

def consumer(q):
    while True:
        item = q.get()
        # print(item)
        if item is None:
            break # Exit if producer signals completion
        print(f"\033[94mConsumer\033[0m got: {item}")
        time.sleep(0.5) # Simulate some work
        q.task_done() # Indicate that the item has been processed

# Create a thread-safe queue
my_queue = queue.Queue()

consumer_thread = threading.Thread(target=consumer, args=(my_queue,))
consumer_thread.start()

producers = []
def multi_thread_producer():
    for i in range(0,11):
        producer_thread = threading.Thread(target=producer, args=(my_queue,i))
        time.sleep(random.random())
        producers.append(producer_thread)
        producer_thread.start()
    my_queue.put(None) # Signal that no more items will be produced


multi_thread_producer()

# Wait for threads to complete

for producer in producers:
    producer.join()
    

consumer_thread.join()

print("All threads finished.")