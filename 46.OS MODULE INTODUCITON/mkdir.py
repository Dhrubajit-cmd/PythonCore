'''
This functions helps to make directories.
'''

import os
# Create a single directory :
os.mkdir("new directory")

# Create a range of directories.

for i in range(0,5):
    os.mkdir(f"new directory/Just Try {i+1}")
