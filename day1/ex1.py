import threading
import time

def worker():
    print("Hello from worker thread")
    time.sleep(1)
    print("Worker from main thread")

print("Hello from main thread")

# create a thread
t = threading.Thread(target=worker)

# start the thread
t.start()

print("Back to main thread")

# will wait heere until the worker thread is finished
t.join()

print("Main thread finished")
