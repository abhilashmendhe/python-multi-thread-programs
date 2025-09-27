import threading

def worker(n):
    print(f"Thread {n} running on {threading.current_thread().name}")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,), name=f"Worker-{i}")
    
    t.start()
    threads.append(t)
    # t.join()
# Wait for all
for t in threads:
    t.join()

print("All threads done!")
