import queue

orders_queue = queue.Queue() # Customer(producer) puts orders in this queue
ready_queue = queue.Queue()  # Chef put meal orders that are completed

