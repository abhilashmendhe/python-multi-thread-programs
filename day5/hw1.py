import threading
from time import sleep
import random

balance = 1000
lock = threading.Lock()

def deposit(amount):
    global balance
    with lock:
        balance += amount
        
def withdraw(amount):
    global balance
    with lock:
        if balance >= amount:
            balance -= amount
        else:
            print(f"Failed withdrawal of {amount:.2f}, balance too low")
            
threads = []
random_amts = []
for i in range(1,10):
    amt = random.random() * 200
    
    trans_ops = random.randint(0,1)
    if trans_ops == 0:
        random_amts.append(("withdraw",amt))
        t = threading.Thread(target=withdraw, args=(amt,))
        t.start()
        threads.append(t)
    else:
        random_amts.append(("deposit",amt))
        t = threading.Thread(target=deposit, args=(amt,))
        t.start()
        threads.append(t)
    

for t in threads:
    t.join()
    
    
# Serial execution to check if balance is equal to parallel balance
serial_balance = 1000
for trans_ops,amt in random_amts:
    if trans_ops == "deposit":
        serial_balance += amt
    else:
        serial_balance -= amt
        
print("Parallel balance: ",balance)
print("Serial balance: ",serial_balance)