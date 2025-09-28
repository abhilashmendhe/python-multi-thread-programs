# 1. Single producer and single consumer

import queue
import threading
import time

def producer(q, num_items):
    for i in range(num_items):
        item = f"Data-{i}"
        q.put(item)
        print(f"\033[91mProducer\033[0m put: {item}")
        time.sleep(0.1) # Simulate some work
    q.put(None) # Signal that no more items will be produced

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break # Exit if producer signals completion
        print(f"\033[94mConsumer\033[0m got: {item}")
        time.sleep(0.2) # Simulate some work
        q.task_done() # Indicate that the item has been processed

# Create a thread-safe queue
my_queue = queue.Queue()

# Create and start producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(my_queue, 5))
consumer_thread = threading.Thread(target=consumer, args=(my_queue,))

producer_thread.start()
consumer_thread.start()

# Wait for threads to complete
producer_thread.join()
consumer_thread.join()

print("All threads finished.")