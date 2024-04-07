from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        exp =i * i
        print(exp)
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

#create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)


#start
for p in processes:
    p.start()

for p in processes:
    p.join()

print('processes are done')

## when running the code, open system information, tasks manager then see how many python
## processes are happening concurrently.