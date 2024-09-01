# Let us talk about TypeCasting.
a = "1"
b = "2"
print(a+b)
# You see this gives 1 + 2 = 12 !!! Is the computer MAD!!!
# NO, it is not mad , when you have entered "1" and "2" as the values of a and b respectively the computer intakes it as str.
# So, when you give the command a+b it takes it as concatenation, i.e it will combine the two values which you must think here,
# so, we get "1"+"2" here as "12"
# But if we put m = 1 and n = 2 then m+n gives the follwing
m = 1
n = 2
print(m+n)

# Now,let us discuss what is Type Casting ?
# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
# Python supports a wide variety of functions or methods like :
# int(),float(),str(),ord(),tuple(),set(),list(),dict(),etc. for the typecasting in python.
c = "1"
d = "2"
print(int(c)+int(d))
# This is called type casting , i.e coversion of one data type into another.
# Similarly we can make
print(float(a)* float(b))
# OR
print(float(c)/float(d))
# But if say
a1 = "Dhrubajit"
a2 = "23"
# Will it work??
## print(int(a1)+ int(a2))
# No, it won't work, because, here, Dhrubajit is a string and it is meaningless to convert it to integer function
#
# There are two types of Type Casting :
# 1. Explicit Conversion (Explicit type casting in python)
# 2. Implicit Conversion (Implicit type casting in python).
#
# Explicit Typecasting :
# The conversion of one data type into another data type , cone via developer or programmer's intervention or manually as per
# the requirement ,is known as explicit type conversion.
#
# It can be achieved with the help of Python's built-in type conversion functions such as int(),float(),hex(),oct(),str(),etc
# Let us see it's example :
# The above shown programs are the examples of Explicit Type Conversion . Where we are manually asking the interpreter to change the
# datatype of the values entered.

# Implicit Typecasting :
# Data types in Python do not have the same level i.e. ordering of data types is not the same in Python.Some of the data types
# have higher-order,and some have lower order.While performing any operations on variables with different data types in Python,
# one of the variable's data types will be changed to higher data type.According to the level,one data type is converted into other
# by the Python interpreter itself(automatically).This is called, implicit typecasting in Python.

# Python converts a samller data type to a higher data type to prevent loss.
# Let us see how it happens :
f = 1.9
g = 8
print(f + g)
# Here, float is generally a higher data-type than the int.So here when we try to add,the interpreter lets f remain float but changes
# the description of g from int to float and hence,renders the result as a flaot value i.e. 9.9.
# This is only called implicit typecasting or type conversion.

