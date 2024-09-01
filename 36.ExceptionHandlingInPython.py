# In this class we shall learn about exception handling in python.

# Let us see how to do it :
# A simple way :
try :
    num = (input("Enter your number:"))
    for i in range(11):
        print(f"{int(num)} X {i} = {int(num) * i}. \n")
except ValueError:
    print(f"{num} is not an integer. \n")

# Other types of error can also be handeled :
try:
   dub = (input("Enter your number: \n"))
   a = [4,5]
   print(a[int(dub)])
except ValueError :
    print(f"{dub} is not an integer. \n")
except IndexError :
    print(f"Index Error. \n")
# Value Error.

# Or
try:
   dub = int(input("Enter your number: \n"))
   a = [4,5]
   print(a[(dub)])
except TypeError :
    print(f"{dub} is not an integer. \n")
except IndexError :
    print(f"Index Error. \n")
# Type error (If incorrect data type entered)

'''
There are many such types of error like, :
RuntimeError
OSError
FileNotFoundError
etc..
Which we shall learn in future. 

'''