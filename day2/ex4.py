import threading

def cube(n, res_arr, idx):
    res_arr[idx] = n ** 3
    

numbers = [1,2,3,4,5]
cube_res = [None] * len(numbers)
threads = []
for idx,num in enumerate(numbers):
    t = threading.Thread(target=cube, args=(num,cube_res, idx))
    t.start()
    threads.append(t)
    

for t in threads:
    t.join()
    
print("Main finished!")
print("Cube results: ",cube_res)