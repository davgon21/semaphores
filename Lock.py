from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value
from multiprocessing import Lock
import time
import random
N = 8
     
def task(common, tid, semaforo):
    for i in range(20):
        print(f'{tid}−{i}: Non−critical Section', flush = True)
        time.sleep(random.random())
        print(f'{tid}−{i}: End of non−critical Section', flush = True)
        semaforo.acquire()
        print(f'{tid}−{i}: Critical section', flush = True)
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section', flush = True)
        time.sleep(random.random())
        common.value = v
        print(f'{tid}−{i}: End of critical section', flush = True)
        semaforo.release()
        
def main():
    lp = []
    common = Value('i', 0)
    semaforo = Lock()
    
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, semaforo)))
    print (f"Valor inicial del contador {common.value}", flush = True)
    for p in lp:
        p.start()
    for p in lp:
        p.join()
    print (f"Valor final del contador {common.value}", flush = True)
    print ("fin")
    
if __name__ == "__main__":
    main()







#Hacer lo mismo con semaforo.Lock() en otro archivo.
