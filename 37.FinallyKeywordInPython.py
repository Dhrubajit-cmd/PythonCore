# In this class we shall learn about the finally keyword in Python.
'''
This is generally used for necessary clean-ups.
'''

try :
    l = [1,2,3,4]
    i = int(input("Enter the index : \n"))
    print(l[i])
except ValueError :
    print("Invalid Datatype. \n")
except IndexError :
    print("Invalid Indexing. \n")
finally :
    print("I am always executed. \n")


'''
You may have the question that , what is the difference between 
try :
    l = [1,2,3,4]
    i = int(input("Enter the index : \n"))
    print(l[i])
except TypeError :
    print(f"Invalid Datatype {i}. \n")
except IndexError :
    print("Invalid Indexing. \n")
print("I am always executed. \n")
And the one done above, i.e why don't we do it this way. It does the same thing the the one at above does.
Then the , difference lies while using it as a funcion and asks the function to return some value. Let's see it.
'''

def func1() :

  try :
    l = [1,2,3,4]
    i = int(input("Enter the index : \n"))
    print(l[i])
    return 1
  except ValueError :
    print("Invalid Datatype. \n")
    return 0
  except IndexError :
    print("Invalid Indexing. \n")
    return 0
  print("I am always executed. \n")

x = func1()
print(x)

# You see print("I am always executed. \n") doesn't get executed.

# But if we use finally :
def func2() :
 try :
    l = [1,2,3,4]
    i = int(input("Enter the index : \n"))
    print(l[i])
    return 1
 except ValueError :
    print("Invalid Datatype. \n")
    return 0
 except IndexError :
    print("Invalid Indexing. \n")
    return 0
 finally :
    print("I am always executed. \n")
x = func2()
print(x)
# The print("I am always executed. \n") will be executed no matter what.