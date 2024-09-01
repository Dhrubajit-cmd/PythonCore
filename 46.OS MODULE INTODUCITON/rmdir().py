import os
# for i in range (0,100) :
#     os.rmdir(f"new folder/Tutorial {i+1}")
# This just directly removes the entire folder.
os.rmdir(f"new folder")




# A way to remove multiple directories with same name inside a directory.
import os
# This command changes the current working directory.
os.chdir("new directory")
# This command helps us to find the path of the directory we are in .
current = os.getcwd()
# The below command just helps us to see the files in the directory.
list = os.listdir(path = current)
print(list)
# The below command actually removes the files from the directory.
for i in range(0,5):
    os.rmdir(f"Just Try {i+1}")
# The below command also makes us see the files inside the directory.
lm = os.listdir(path = current)
print(lm)




