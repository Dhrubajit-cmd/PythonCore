# In this class we shall learn about Multithreading in Python .

from threading import Thread # or you can import directly the threading module , but have to write threading.Thread to thread a process/variable.
import time
from concurrent.futures import ThreadPoolExecutor
def function(seconds):  # Indicates some task being done.
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
time1 = time.perf_counter()  # Used for performance counting
# Normal Method :
function(4)
function(2)
function(1)
time2 = time.perf_counter()
print(time2 - time1)

time3 = time.perf_counter()
# Using Threads : Makes the process faster as it helps the codes to run parallely.
t1 = Thread(target = function, args = [4])
t2 = Thread(target = function, args = [2])
t3 = Thread(target = function, args = [1])

t1.start()  # Chalu kar do background mein aur aage badho. Yeh rukta nahi hain poora execute hone tak. Toh t3.start() ke case mein bhi yeh bina ruke hi next lines ko execute
t2.start()  # kar diya jiske chalte hame mila ki yeh process almost 0 sec mein hi khatam ho gaya.
t3.start()
# Agar hamein rukna hain toh
t1.join()
t2.join()
t3.join() # Yeh dal denge toh yeh t3 ke khatam hone tak rukega phir doosra line of code run karega.


time4 = time.perf_counter()

print(time4 - time3)


def poolingDemo():
    with ThreadPoolExecutor() as executor :
        future = executor.submit(function,3)
        print(future.result())
        future = executor.submit(function,2)
        print(future.result())
        future = executor.submit(function,4)
        print(future.result())

poolingDemo()