# In this class we shall learn about the time module in Python.
import time
def usingWhile() :
    i = 0
    while i < 50000 :
        i = i + 1
        print(i)
def usingFor() :
    for i in range(50000):
        print(i)

init = time.time()
usingFor()
print(time.time() - init)


time_init = time.time()
usingWhile()
print(time.time() - time_init)


print(4)
time.sleep(3) # Iske baad ke code ko specified time tak ruka deta hain.
print("This is printed after 3 seconds. \n")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t) # Month Aur Date ke liye small letter. Aur Year ke liye cap, H , M ,S ke liye capital.
print(formatted_time)