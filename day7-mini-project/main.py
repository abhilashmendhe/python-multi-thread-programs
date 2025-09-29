from customer_producer import customer_create_orders
from chef_consumer_producer import chef_prepares_order
from waiter_consumer import run_waiter_service
from channels import orders_queue, ready_queue
import threading

CUSTOMERS = 10
CHEFS = 2
WAITERS = 6

waiter_serve_threads = run_waiter_service(WAITERS)
chef_prepares_threads = chef_prepares_order(CHEFS, WAITERS)
customer_orders_threads = customer_create_orders(CUSTOMERS, CHEFS)

def wait_signal_chefs():
    for cp in chef_prepares_threads:
        cp.join()
    for _ in range(WAITERS):
        ready_queue.put(None)

signal_thread = threading.Thread(target=wait_signal_chefs, daemon=True)
signal_thread.start()

for co in customer_orders_threads:
    co.join()

signal_thread.join()

for wp in waiter_serve_threads:
    wp.join()

orders_queue.join()
ready_queue.join()

print(f"\nOrders left unprocessed: {orders_queue.qsize()}")
print(f"Dishes left unserved: {ready_queue.qsize()}")
print("\nAll dishes completed.... Restaurant is closing...")