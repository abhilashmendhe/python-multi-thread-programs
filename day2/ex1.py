import threading

def worker():
    print(f"Running in thread: {threading.current_thread().name}")

# Default names
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

# Custom name
t3 = threading.Thread(target=worker, name="MyWorker")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
