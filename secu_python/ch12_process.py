import multiprocessing
import time
import random
import os

def worker():
    n = random.randint(1, 100)
    print(f"PID {os.getpid()} génère le nombre {n}")
    time.sleep(60)  

if __name__ == "__main__":
    processes = []
    for _ in range(5):  
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

    print("Close process")
