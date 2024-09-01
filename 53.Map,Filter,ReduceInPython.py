# In this class we shall learn about Map,Filter,Reduce in Python.

# Map, Filter and Reduce :
'''
In python , the map , filter and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as
higher-order functions , as they take other functions as arguments.
'''

# Map :
'''
The map functions applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax :
map(function , iterable)
The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple or any other iterable object. 
Here, is an example how to use map function :
'''
def cube(x):
    return x * x * x
l = [1,2,4,6,4,3]
newl = []
for item in l :
    newl.append(cube(item))
print(newl)

# A way to do this using map :
nexl = list(map(cube,l))
print(nexl)

# Now can we make it more simple using the Lambda function ? Answer is : YES !!
square = lambda x: x*x
list0 = [1,2,3,4,5,6]
mapping = list(map(square,list0))
print(mapping)

# See we have just replaced the 7 lines of code into 4 lines of code using lambda and map, which makes our code efficient . Is it readable ? : Yes, in some cases and No, in other cases. It depends.

# Filter :
'''
The filter function filters a sequence of elements based on a given predicate(a function that returns a boolean value) and returns a new sequence containing only the elements that meet the
predicate . The filter function has the following syntax :

filter(predicate, iterable)

The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple or any other iterable object. 
'''
def filter_function(a) :
    return a > 4
new_l = filter(filter_function,l)
print(new_l)
# This shall give filter object . Now, if you want list object you can do it using the list .
newx_l = list(filter(filter_function,l))
print(newx_l)

# Reduce :
'''
The reduce function is a higer-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax :
reduce(function,iterable)

The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements and so on . The reduce function returns the final result. 

Here is an example of how to use reduce function :
'''
# We need to import reduce :
from functools import reduce
numbers_list = [1,2,3,4,5,6,7,8,9,10]
def mysum(x,y):
    return x+y
suml = reduce(mysum,numbers_list)
print(suml)
