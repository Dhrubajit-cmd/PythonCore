# In this class we shall learn about the tuple methods in Python .
# Manipulating Tuples :
# Tuples are immutable , hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform
# operation on that list and convert it back to tuple .
# As, tuples are immutable so, we need to convert it into list first,then make the changes and then again convert it into a list.
tup = ("Hello",1,3,656,"Ramu","Rajiv","Delhi",4567)
print(tup)
temp = list(tup)
temp.append(34)
temp.pop(3)
temp[2] = "INDIA"
tup = tuple(temp)
print(tup)

# Now, let us look upon some tuple methods.
# 1.count() method :
cnt = tup.count("Ramu")
print(cnt)
# It counts how many times an element has occured .

# 2. index() method :
# The index() method returns the first occurence of the given element from the tuple .
print(tup)
mn = tup.index("Ramu")
print(mn)
res = tup.index(4567)
print(res)

# This is all in Tuples.
# We shall get to learn further more in future.But, for now this is it.

