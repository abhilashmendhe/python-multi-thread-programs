import threading
from time import sleep

def worker(num):
    for i in range(1, 6):  # print 1 to 5
        print(f"Thread {num}: {i}")
        sleep(0.5)

threads = []
for i in range(2):  # try with 2 threads first
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Main thread does its own work
for _ in range(5):
    print("Main is working...")
    sleep(0.5)

# Now wait for threads to finish
for t in threads:
    t.join()

print("All threads finished")

