import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # no lock

threads = []
start_time = time.time()

for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print("Without lock - Final counter:", counter)
print(f"Elapsed time: {end_time - start_time:.4f} seconds")
