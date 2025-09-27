import threading
from time import sleep

def worker(main_alive):
    while not main_alive.is_set():
        print("Logging......")
        sleep(1)

# main_alive = True
main_alive = threading.Event()
t = threading.Thread(target=worker, daemon=True, args=(main_alive,))
t.start()

i = 1
while True:
    if i > 5:
        main_alive.set()
        break
    print("I am main thread step:",i)
    sleep(1)
    i += 1
    
    