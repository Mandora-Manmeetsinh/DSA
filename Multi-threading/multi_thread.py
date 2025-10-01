import threading
import time

def func(seconds) :
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
func(4)                                 # Normel code
func(2)
func(1)
time2 = time.perf_counter()
print(time2 - time1)

# ========================================================= #

time1 = time.perf_counter()
t1 = threading.Thread(target=func , args=[4])      # code using threads
t2 = threading.Thread(target=func , args=[2])
t3 = threading.Thread(target=func , args=[1]) 

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(f"The time required to complete the function {time2 - time1}") 