"""
    Day 11: ThreadPoolExecutor
"""

from concurrent.futures import ThreadPoolExecutor
import time
import random

def square(n):
    print(f"Calculating square of {n}")
    time.sleep(random.uniform(1, 3))  # simulate work
    result = n * n
    print(f"Square of {n} is {result}")
    return result
    

numbers = [1,2,3,4,5]

with ThreadPoolExecutor(max_workers=4) as executor: 
    futures = [executor.submit(square, n) for n in numbers]
    
    for future in futures:
        print("Result:", future.result())

print("All calculations complete!")