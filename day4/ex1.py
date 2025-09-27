import threading 
import time

def background_task():
    while True:
        print("Daemon thread is running....")
        time.sleep(1)
        
# Mark as daemon
t = threading.Thread(target=background_task, daemon=True) # daemon=False
t.start()

print("Main thread sleeping for 3 seconds...")
time.sleep(3)
print("Main thread finished")

t.join()