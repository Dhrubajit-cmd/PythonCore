# In this class we shall learn about For Loops in Python. Let's get started .
# So, what are loops ?
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on
# this loops are further classified into following types : for loop , while loop , nested loop .

## FOR LOOP :
# For loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings,
# lists, tuples , sets and dictionaries.

# A simple code in for based on integer :
for i in range (21) :
    print(i)
# A simple code in for loop based on strings :
def namelower():
 name = "Dhrubajit Chakravarty"
 for i in  name :
    print(i)
  ## You can also use if-else here if you wan't it.
    if (i == "C") :
        print(i.lower())
    # This particular code after entering into C , it lowers it , as per the demand set by me

# Let us call a function based on it .
# Now check after calling it .
namelower()

# Now , let's iterate it in lists.
def colourcheck() :
 colours = ["Red","Blue","Green","Yellow","Purple","Orange","White","Black"]
 for x in colours :
    print(x)
    if (x == "Red") :
        print("The colour is a primary colour.")
    elif (x == "Blue") :
        print("The colour is a primary colour.")
    elif (x == "Green") :
        print("The colour is a primary colour.")
    else :
        print("The colour is a secondary colour.")
# Now let's call and check it
colourcheck()

# Let's see the use of step :
for i in range(0,10,2):
    print(i)
# Here step means , ignoring or jumping steps , here it jumps 2 steps like after printing 0 it steps 2 and prints 2 and similarly
# repeats it until it reaches the end i.e 8 or you can make it upto 10 your choice . You see, this code basically prints the even
# nos from 0 to 8 . See , so simple way to do it .
for i in range(0,12):
    if (i%2) == 0 :
        print(i)
# % means the result will be the reminder.

# This is all about basics of For Loop and its uses.
