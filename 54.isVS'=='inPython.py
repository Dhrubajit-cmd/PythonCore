# In this class we shall learn about the difference between is and '=='.

a = 4
b = 4
if a is b : # exact location of object in memory
    print(True)
if a == b : # value
    print(True)
# IF
c = 4
d = "4"
if c is d:
    print(True)
if c == d :
    print(True)
else :
    print(False)
# Neither they are same nor they have same memory allocation .

# next case :
m = [1,2,34]
n = [1,2,34]
print(m is n) # Bhai yahan false because lists are mutable,they can be changed hence,python allocates different memory to them though they look alike
print(m == n) # But they have same values hence we get true.

# Confusing case :
x = 3
y = 3
print(x is y)# They are immutable hence, a x and y both are given 3.Toh yeh space waste n karke allocates same memory to both.
print(x == y)

# Doubt Clearing case:
l = (1,2,34)
o = (1,2,34)
print(l is o)# True because tuples are immutable.
print(l == o)

# Misellaneous :
f = None
g = None
print(f is g) # Prints True
print(f == g)
print(f is None) # Prints true same with g