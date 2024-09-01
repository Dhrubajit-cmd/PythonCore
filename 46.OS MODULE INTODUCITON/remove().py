'''
This command helps us to remove a file from a directory.
'''
import os
current = os.chdir("new directory")
path = os.getcwd()
print(path)
list = os.listdir(current)
print(list)
# Create a new file into the empty directory .
f = open("main.py","a+")

# If you run and check you will see a new file created.

list0 = os.listdir(path ='/home/dc/Documents/PYTHON/Python Core/46.OS MODULE INTODUCITON/new directory')
print(list0)

dash = os.remove("main.py")
list1 = os.listdir(path = '/home/dc/Documents/PYTHON/Python Core/46.OS MODULE INTODUCITON/new directory')
print(list1)




# You can see first the folder was empty then we see a new file created and after removing we see that the folder is empty again .
