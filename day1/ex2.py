import threading
from time import sleep

def worker(num):
    for i in range(1,10): 
        print(f"Thread {num}:{i} is running")
        sleep(0.5)

threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for _ in range(5):
    print("Main is working...")
    sleep(.5)

# now join/wait the threads
for t in threads:
    t.join()
#    pass


print("All threads finished")
