# Let us now talk about Strings in python.
name = "Dhrubajit"
friend = "Dishant"
anotherFriend = "Raj"
print("Hello," + name)
# If we want to print multi-line string, we can proceed this way.We,can use triple single quote or triple double quote.
str = '''Hello Dhrubajit,
how are you,
what are you doing'''
print(str)

# If we wan't to do indexing,that also we can do using strings. Let's see how to do it .
print(name[0])
print(name[1])
print(name[-1])
# But if we give
# print(name[9])
# We get ERROR as, this doesn't exist.

# We can LOOP through strings using FOR LOOP.
# The code below prints all the characters in the string one by one
print("Here,we are printing each character of name \n")
for character in name:
    print(character)
# OR
print("Here we are printing each character of str \n")
for character in str:
    print(character)
