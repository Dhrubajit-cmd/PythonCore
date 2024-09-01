# In this class we shall learn about the Local as well as the Global variables in Python.

# Let us understand it with an example :
x = 10 # Global Variable
print(x)

def my_function() :
    global x
    x = 67 # This takes the global value of x and changes it to 67, now check it shall show 67 as we print it at the last line.
    # Similarly we can define y globally this way
    global y
    y = 5 # Local Variable
    print(y)
my_function()
print(x)
'''
print(y) . This command shall give an error as , we haven't defined y globally. One may ask, but y is defined under my_funciton() ? Yes, it is , i.e it is a local variable.
That is we have defined it but , it is local to my_function , but not global to the (file).py whatever the file name is. Now, what if we want to change the global value inside
the local value just use the global keyword. 
'''
# Now see, the print(y) command shall not give error. Instead it gives the globally defined value i.e 5.
print(y)

# This is all about local and global variable and the global keyword.
