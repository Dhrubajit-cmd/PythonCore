# What is Function Cashing ? :
# Just see the example :
import functools
import time
# Isko import karne ka ek aur tarika hain :
# from functools import lru_cache
# toh phir @functools.lru_cache(maxsize = None) nahi dalke @lru_cache(maxsize = None) chalane se bhi hoga.
@functools.lru_cache(maxsize = None)
def fx(n):
    time.sleep(5)
    return n * 5

print(fx(20))
print("Done For 20 \n")
print(fx(6))
print("Done For 6 \n")
print(fx(2))
print("Done For 2 \n")

print("Done For 20 \n")
print(fx(6))
print("Done For 6 \n")
print(fx(2))
print("Done For 2 \n")

