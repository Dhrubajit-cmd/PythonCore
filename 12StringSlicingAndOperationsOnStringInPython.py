# In this class we shall talk about string slicing.
a = "Dhrubajit"
# We can find the length of a string using len() function.
# Example has been shown below
print(len(a))
# This shall give the length of the function.
# Another example
fruit = input("Enter any fruit name of your choice. \n")
len1 = len(fruit)
# print(fruit , "is a" , len , "letter word.")
# The above program , takes the input of any fruit name from the user and says how many letters are there in it's spelling.
print(f"{fruit} is a {len1} letter word \n")
# You see the above line also shows the use of the f string used before the inverted commas, it makes writing the code much easier.


## Now let's discuss about String Slicing
# Remember square brackets are used in slicing not parenthesis.
print(a[0:6])
# The above written code represents string slicing.This is used to print the characters in the string as per the specified value input
# by the programmer.
print(a[:6])
# Also,gives the same value hence it will put zero itself
print(a[:])
# Here, python automatically puts 0 at the start and len(a) at the end.
## Negative slicing :-
print(a[0:-3]) #1
# OR
print(a[0:len(a)-3])
# This is what the #1 code means, computer puts len(a) automatically , for your convenience always count it this way to get the correct answer.
# Remember it displays one less than the value obtained.

## Loop Through a String :
# Strings are arrays and arrays are iterable.Thus,we can loop through strings.
name = "Ajit"
for i in name:
    print(i)

# Quick Quiz :
# Predict the output:
nm = "Harry"
print(nm[-4:-2])
# The output will be "ar"
# Check by running.

