# In this class we shall learn about dictionaries in Python.

# What are dictionaries in python ?
'''
Dictionaries are ordered collection of data items.They store multiple items in a single variable. Dictionary items are key-value
pairs that are separated by commas and enclosed within curly brackets{}.
'''
# Example :
info = {"Name":"Dhrubajit Chakravarty","Age":19,"Course":"Computer Science Engineering","Year":"1st Year"}
print(info)
print(type(info))
# Two methods to get it :
print(info["Name"]) # Here, Name is key : Dhrubajit Chakravarty is value
print(info.get("Name"))
# But one thing if :
# print(info["Name2"]) # Gives Error
print(info.get("Name2")) # Returns None

# Two ways to print all keys :
print(info.keys())
# OR
for key in info :
    print(info[key])
# To get values :
print(info.values())

# To print key value pairs :
print(info.items())
# OR
for key,value in info.items() :
    print(f"The value corresponding to the {key} is {value}. \n")

# Next class we shall learn about dictionary methods in python.
