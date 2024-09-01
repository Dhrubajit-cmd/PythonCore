a = "Dhrubajit !!!"
# A code to check the length of the string
print(len(a))
# What to do if we want to convert the letters of the string in upper-case.
# Remember, the strings are immutable
# So,
# If we do:
print(a.upper())
# We get a different{new} string, with upper-case letters, it is not that the values of the previous string has changed.This is because
# strings are immutable.

# There is also a code to convert the literals of our string to lower-case.
print(a.lower())
# This also creates a {new} string with just lower-case letters in it.


# The code rstrip() is used to remove any trailing characters in a string.Let us see how to do it.
print(a.rstrip("!"))
#
m = "Dhrubajit"
print(m.rstrip("it"))

# The replace() method replaces all occurences of a string with another string. Example :
str2 = "Harry is a good boy!!"
print(str2)
print(str2.replace("Harry","Dhrubajit"))

# The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(str2.split(" "))
# The above command separates all the space separated words and puts them into a list.
print(m.split("r"))
# The above command takes "r" in m as the separator and puts the other two separated values into a list.


## Capitalize() Method:
# The capitalize() method turns only the first character of the string to uppercase and the rest other character of the string
# are turned to lowercase.The string has no effect if the first character is already uppercase.
# Example :
cap1 = "abhishruti"
print(cap1.capitalize())
cap2 = "hello WorlD"
print(cap2.capitalize())

## Center() Method:
# The center() method aligns the string to the center as per the parameters given by the user.
# Example :
cent1 = "Welcome to the Console"
# print(cent1.center(200))
print(cent1.center(200,"."))
# Width here, is width
# _fillchar here is the character that is to be applied to the rest of the spaces.

## Count() Method :
# The  count() method returns the number of times the given value has occurred within the given string.
count1 = ("Transformers : The Rise of The Fallen")
print(count1.count("T"))

## Endswith() Method :
# The endswith() method checks if the string ends with a given value. If yes then return True,else returns False.
end1 = "Hello World !!"
print(end1.endswith("!!"))
print(end1.endswith("ru"))
print(end1.endswith("ll", 1,4))

## Find Method :
# The find() method searches for the first occurence of the given value and returns the index where it is present. If given
# value is absent from the string then return -1.
find1 = "He's name is Dan. He is an honest man."
print(find1.find("Dan"))
print(find1.find("is"))
# For -1
print(find1.find("ishh"))
#  The above code shall print -1 as there is no presence of ishh in the statement.
# In place of find() if we use index() this shall return an error
# print(find1.index("ishh"))

## Isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z,a-z,0-9.If any other characters or punctuations
# are present,then it returns False.
alnum1 = "Hello @ Dhurbajit 0149C8"
print(alnum1.isalnum())
# But for this :
alnum2 = "HelloDhrubajit0149C8"
print(alnum2.isalnum())
# It shall print True in return.
# Even if space is kept in between it returns False.


## Isalpha() :
# The isalpha() method returns True only if the entire string only consists of A-Z,a-z,0-9.If any other characters or punctuations
# are present,then it returns False.
# Example :
alpha1 = "HelloWorld"
print(alpha1.isalpha())
# But if we give
alpha2 = "HelloWorld!!"
print(alpha2.isalpha())
# OR
alpha3 = "Hello World"
print(alpha3.isalpha())
# It shall return False as the value.

## Islower() :
# The islower() method returns True only if all the characters in the string are lower case,else it returns False.
# Example :
lower1 = "hello"
print(lower1.islower())
# But if we give
lower2 = "Hello"
print(lower2.islower())
# It shall return False.

## Isprintable() :
# The isprintable() method returns True if all the values within the given string are printable,if not, the returns False.
# Example :
print1 = "We wish you a Merry Christmas."
print(print1.isprintable())
# But if we write
print2 = "We wish you a Merry Christmas. \n"
print(print2.isprintable())
# It shall return False. As, \n is not printable .


## Isspace() :
# The issapce() method returns True only and only if the string contains white spaces,else returns False.
space1 = "            " # Space using spacebar
print(space1.isspace())
space2 = "            " # Space using TAB
print(space2.isspace())
# They both shall return true.
# But
nospace = "Hey man how are you"
print(nospace.isspace())
# Shall return False.

## Istitle() :
# The istitle() method returns True only if the first letter of each word of the string is capitalized,else it returns False.
title = "Hello World"
print(title.istitle())
# Shall print True.
# But
title1 = "Hello world"
print(title1.istitle())
# Shall print False.


## Similarly , there are many like
# Isupper() : , Similar to islower()
## Startswith() :
start = "Hi I am Dhruba"
print(start.startswith("Hi"))
# Prints True.
print(start.startswith("Hello"))
# Prints False.

# Similarly ,endswith():

## Swapcase() :
# The swapcase() method converts lowercase to uppercase and vice versa.
swap = "HellO WoRLd"
print(swap.swapcase())

## Title() :
# The title() method capitalizes first letter of each word within the string.
titi = "His name is Dan. he is a good boy."
print(titi.title())


## These are some important string methods that are useful in Python.