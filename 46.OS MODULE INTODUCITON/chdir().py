'''
This function is used to change the current working directory.
'''
import os
print("Previous Working Directory:",os.getcwd())

os.chdir("new directory")

print("Current Working Directory:",os.getcwd())


