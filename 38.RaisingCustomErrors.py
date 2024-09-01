# In this class we shall learn about how to raise custom errors in python.

# Let's raise a simple error :
print("Question: Print the table of any number between 5 and 9 . \n")
# Here, in order to make the code smooth we can raise an error and stop the program there itself if the user enters a another value. This is where raising an error is useful.
a = int(input("Enter the number between 5 and 9 : \n"))
if(a < 5  or a > 9 ):
    raise ValueError(f"{a} is not between 5 and 9. \n")
for i in range(1,11):
    print(f"{a}X{i} = {a*i}")

# Defining Custom Exceptions :
'''
In python we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
'''
# Exceptions :
# class CustomError(Exception):
#     # code ...
#     pass
# try :
#     # code..
# except CustomError:
#     # code..
'''
This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.
'''

# Quick Quiz
'''
Quesion : The same program must run , but if user gives quit as input , it must not raise an error.
'''
# QUIT - NO ERROR
# ANYTHING ELSE - ERROR
try :
  num  = input("Enter the number between 5 and 9: \n")
  if (num == 'quit') :
      print("Okay exitting... \n")
  else:
     if (int(num) < 5 or int(num) > 9) :
       raise ValueError(f"{int(num)} is not between 5 and 9. \n")
#except ValueError :
   # print(f"{num} is not an integer. \n")
finally :
    print("Program is executed. \n")
