# In this class we shall learn about the Shutil Module in Python.

import shutil
import os

shutil.copy("87.ShutilModuleInPython.py","Copy.py") # Copies a file from source and saves it into a destination

shutil.copytree("43.VirtualEnvironment","CopyTree") # Copies a directory. He he

# Similarly, shutil.move() can move from one point to another(destination).

# shutil.rmtree helps us delete a folder.
shutil.rmtree("CopyTree")

# os.remove can delete a file programatically.

os.remove("Copy.py")


# This is only with shutil , easy peasy .