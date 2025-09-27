import threading

def square(n):
    print(f"Square of {n} is {n*n}")
    

numbers = [1,2,3,4,5]

threads = []
for num in numbers:
    t = threading.Thread(target=square, args=(num,))
    t.start()
    threads.append(t)
    

for t in threads:
    t.join()
    
print("Main finished!")