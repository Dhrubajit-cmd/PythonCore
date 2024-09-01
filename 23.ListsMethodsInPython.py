l = [1,2,3,4,5,6,7,8]
print(l)
l.append(9)
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.count(1))
# Another process to change list
m = l
m[0] = 0
print(l)
# Insert
l.insert(1,899)
print(l)
# Concatenation of two lists.
# Matlab , j ko kholo aur uske values ko l ke end pe rakh do. Simple meaning .
j = [900,1000,1100]
l.extend(j)
print(l)
# Another way of concatenation if we don't wan't to change l
k = l + j
print(k)

# There are many other methods in lists.Which I will learn further and keep on adding here.
# But for now that's it .

