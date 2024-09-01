# In this class we shall learn about Enumerate Function in Python.
'''
The enumerate function is a built-in function in Python that allows you to loop over a sequence(such as lists,tuple or string) and get the
index and value of each element in the sequence at the same time. Here's a basic example of how it works.
'''
# Loop over a list and print the index and value of each element .
fruits = ['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)


marks = (44,45,76,89,98,17)

for index,mark in enumerate(marks):
    print(index,mark)

# If we want to start the index with 1 then :

for index,mark in enumerate(marks,start=1):
    print(index,marks)


# This is all in enumerate.

names = ["Dhrubajit ", "Raj", "Dishant", "Ananya"]
for index,name in enumerate(names, start = 1):
    print(index,name)