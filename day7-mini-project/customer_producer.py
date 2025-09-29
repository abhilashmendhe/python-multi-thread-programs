import threading
import time 
from typing import *
import queue
import random
from channels import orders_queue

def customer_producer(q: queue.Queue, cust_id: int, dish: str):
    q.put((cust_id,dish))
    print(f"\033[95mCustomer {cust_id}\033[0m ordered food: {dish}")
    
def customer_create_orders(num_customer: int, num_chefs: int):
    
    customer_threads = []
    dishes = ["fish soup", "chicken pasta", "lasagna", "pancakes", "biryani", "lemonade", "raviolli", "burger", "fries"]
    
    for cust_id in range(num_customer):
        dish_ind = random.randint(0, len(dishes)-1)
        cust_thread = threading.Thread(target=customer_producer, args=(orders_queue, cust_id, dishes[dish_ind]))
        customer_threads.append(cust_thread)
        time.sleep(random.random())
        cust_thread.start()

    for _ in range(num_chefs):
        orders_queue.put(None)
        
    return customer_threads