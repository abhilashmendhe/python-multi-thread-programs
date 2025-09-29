from channels import ready_queue
import threading, queue, time, random

def waiter_consumer(r_q: queue.Queue, waiter_id: int):
    
    while True:
        
        task = r_q.get()
        if task is None:
            r_q.task_done()
            print(f"\033[92mWaiter-{waiter_id}\033[0m has no food to serve. Exiting...")
            break 
        cust_id, dish = task 
        time.sleep(random.random()*2)
        print(f"\033[93mWaiter-{waiter_id}\033[0m served dish: {dish} to customer-{cust_id}")
        r_q.task_done() 


def run_waiter_service(num_waiters):
    
    waiter_threads = []
    
    for waiter_id in range(num_waiters):
        waiter_consume_thread = threading.Thread(target=waiter_consumer, args=(ready_queue, waiter_id))
        waiter_consume_thread.start()
        waiter_threads.append(waiter_consume_thread)

    return waiter_threads