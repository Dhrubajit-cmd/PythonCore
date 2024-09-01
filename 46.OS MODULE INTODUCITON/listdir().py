'''
listdir() helps us to list us all the present files and directories that can be worked
upon in a specified path.
'''

import os
# current_dir = os.getcwd()
# print(current_dir)
list = os.listdir(path ="/home/dc/Documents/PYTHON/Python Core")
# Agar ek ek karke print karna hain toh , you can do it this way :
for folder in list :
    print(folder)






