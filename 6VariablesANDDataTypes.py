# In this class we shall talk about the Variables and Data Types.
# Let us first talk about variables.
# Variable is a container that stores data.Very similar to how our containers in kitchen holds sugar,salt etc.Creating a variable is like creating
# a placeholder in memory and assigning it some value. In Python its as easy as writing:
# a = 1
# b = True
# c = "Dhrubajit"
# d = None
a = 1
print(a)
b = "Dhrubajit"
print(b)

# Now let's talk about datatypes
# What is a Data Type ?
# Data type specifies the type of value a variable holds.This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:
m = 23
print(type(m))
n = "1"
print(type(n))
# By default python provides the following built in data types.
# 1. Numeric data: int,float,complex
# . int : 3,-8,0
# . float: 3.1,-2.3,0.00001
# . complex: 6+2i
# 2. Text data : str
# # . str : "Hello World" , "Python Programming"
# 3. Boolean Data :
# Boolean data consists of values True or False.
# Example :-
l = True
print(type(l))
# 4. Sequenced data : list, tuple:
# . list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.Lists are mutable and can
# be modified after creation.
# Example:
list1 = [3,4,5,"Name","Dhrubajit",True,None]
print(list1)
# . tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parenthesis.Tuples are immutable and cannot
# be modified after creation.
# Example :-
tuple1 = (1,4,"Dhrubajit",False,None)
print(tuple1)
# 5. Mapped Data : dict
# . dict : A dictionary is an unordered collection of data containing a key:value pair.The key:value pairs are enclosed within curly brackets.
# Example :
dict1 = {"name":"Dhruba","age":19,"canVote":True}
print(dict1)