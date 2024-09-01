## Let us first know, what are Match Case Statements ?
# To implement switch-case like characteristics very similar to if-else functionality,we use a match case in python. If you are coming from a
# C , C++ or Java like language , you must have heard of switch-case statements. If this is your first language , don't worry as I will tell
# you everything you need to know about match case statements in this class.

# A match statement will compare a given variable's value to different shapes,also referred to as the pattern. The main idea is to keep on comparing
# the variable with all the present patterns until it fits into one.

# The match case consists of three different entities :
# 1. The match keyword.
# 2. One or more case elements.
# 3. Expression for each case.
#
# The case clause consists of a pattern to be matched to the variable , a condition to be evaluated if the pattern matches, and a set of statements
# to be executed if the pattern matches.

# A simple program to understand the syntax and use of match case statements.
x = int(input('Enter the number : \n'))
# x is the variable to match
match x :
    # if x is 0
    case 0 :
        print(x)
    # if x is 1
    case 1 :
        print(x +1)
    # if x is 2
    case 2 :
        print(x + 2)
    # if x is default (or) any other number
    # case _ :
    #     print(x + 100)

    # Default can have four cases like :
    case _ if x != 90:
        print("X is not equal to 90")
    case _ if x != 80:
        print("X is not equal to 80")


