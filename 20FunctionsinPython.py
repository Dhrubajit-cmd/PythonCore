# We shall learn about functions in this class.
# What is a function ?
# Function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amount of code
# it is advisable to create or use existing fucntions that makes the program flow organized and neat.
# There are two types of functions :
# 1. Built-in functions .
# 2. User-defined functions .

## Built-in functions :
# These functions are defined are pre-coded in python. Some example of built-in functions are as follows :
# min() , max() , len() , sum() , type() , range() , dict() , list() , tuple() , set() , print() etc.

## User defined functions :
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
# Let us see what is the Syntax to do it :
def function_name () :
    print("Ram")
def apifunction () :
    print("Raghu Nandan Hanuman ")
function_name()
apifunction()
# The below code is a wrong code.
# def namefunction() :
#     truename = "Dhrubajit"
#     while (naam != truename):
#         naam = input(print("Enter your name: \n"))
#         str = "Password"
#         while (passwd != str):
#             passwd = input(print("Enter your password \n"))
#     else :
#         print("Please enter your correct name.")
#
# namefunction()

# The below code is a corrected version of it . Remember, whenever you decide to use a variable in while  make sure to define it before using
# it in while .
def namefunction():
    truename = "Dhrubajit"
    truepass = "Password"

    naam = input("Enter your name: \n")

    while (naam != truename):
        print("Please enter your correct name.")
        naam = input("Enter your name: \n")

    passwd = input("Enter your password: \n")

    while (passwd != truepass):
        print("Please enter your correct password.")
        passwd = input("Enter your password: \n")

    print("Welcome,", truename)
namefunction()
# This is a very important thing that you very often forget.

# Let us create a function to find the sum of two numbers.
def sumcalc() :
    a = float(input("Enter the first number : \n"))
    b = float(input("Enter the second number : \n"))
    add = a + b
    print(f"The two numbers are {a} and {b}.And their sum is : {add}")
sumcalc()
def subcalc() :
    print("We shall make it later someday. \n")
subcalc()
def mulcalc() :
    print("We shall make it later someday. \n")
mulcalc()


def hehe() :
    pass
# This passes the functions kind off you can do it later(Complete it later).
