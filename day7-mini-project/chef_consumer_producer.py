from channels import orders_queue, ready_queue
import queue
import threading
import time 
import random 

def chef_consumer(order_q: queue.Queue, ready_q:queue.Queue, chef_id: int):
    
    while True:
        
        task = order_q.get()
        if task is None:
            order_q.task_done()
            print(f"\033[92mChef-{chef_id}\033[0m has already prepared the food and/or no task left. Exiting...")
            break    
        cust_id, dish = task 
        print(f"\033[94mChef-{chef_id}\033[0m preparing dish: {dish} for customer-{cust_id}")
        time.sleep(random.random()*3)
        ready_q.put(task)
        print(f"\033[46mOrder for customer-{cust_id} prepared by chef-{chef_id}!!\033[0m")
        order_q.task_done()     


def chef_prepares_order(num_chef: int, num_waiters: int):
    
    chef_consumers_threads = []
    for chef_id in range(num_chef):
        chef_consume_thread = threading.Thread(target=chef_consumer, args=(orders_queue, ready_queue, chef_id))
        chef_consume_thread.start()
        chef_consumers_threads.append(chef_consume_thread)

    return chef_consumers_threads
