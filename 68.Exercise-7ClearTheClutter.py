# Question :
'''
Write a program to clear the clutter inside a folder on your computer.
You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file format.
'''

# Solution :

import os

files = os.listdir("clutteredfolder")
i = 1
for file in files :
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredfloder/{file}", f"clutteredfolder/{i}.png")
        i = i + 1



# This is the solution yaar , simple as ****..