# In this class we shall learn about tuples in python.
# Remember Tuples are immutable.
tup = (1,3,9)
print(type(tup))
#  The above is an example of tuple.
# tup.append(4)
# print(tup)
print(tup[0:3])
print(tup[:-2])
# See Indexing is also available in Tuples.
print(len(tup))
if 1 in tup :
    print(True)
else :
    print(False)
# See you  can also use if-else statement with tuples.
# If we do this :
tup2 = tup[1:4]
print(tup2)
# This doesn't change the previously made tuple but just makes a new tuple. As, evident in the code above and it's output.
# You can also use jump index here :
tupa = (1,2,3,4,5,6,7,8,9,10,11)
print(len(tupa))
print(type(tupa))
print(tupa[0:11:2])
tus = (i for i in tupa if i%2 == 0)
print(list(tus))
print(type(tus))

# This is all about introduction in Tuples .
# In next class we shall learn about Methods in Tuples.
