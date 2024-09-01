# In this class we shall talk about how to take user input using python .
# Let us see how to actually do it .
# Example :
a = input("Please enter the user name-\n")
print("Hello",a)
# The above command will take the user's name as an input from the user .

# Now, there is a basic thing to understand in this user input system.
# Let's see what it is
x = input("Enter the first number: \n")
y = input("Enter the second number: \n")
print(x+y)
# This gives a basic addition error.....
# This happens because the number we have entered is done as a string and as you know, sting concatenates, i.e , let's say if
# we input 100 and 123 as the two numbers then their x+y shall give 100123. {Wrong Addition!!!!}
# In order to resolve this we need to understand the fact that the numbers that we input must be in int() or float() to function
# the arithmetic operations.
# See the below example to understand.
# We take the same case, but now in a different manner.
x1 = int(input("Enter the first number: \n"))
y1 = int(input("Enter the second number: \n"))
print(x1+y1)
# See, this gives the correct addition as expected.As, we have input it as integers.The same can be done as float.
x2 = float(input("Enter the first number: \n"))
y2 = float(input("Enter the second number: \n"))
print(x2+y2)
# This also gives the correct answer but now in a more accurate manner as this involves the decimals too.
