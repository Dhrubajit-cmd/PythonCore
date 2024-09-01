# In this class we shall learn about File Handling in Python.

# Opening a File :
'''
Python , open() function helps us to open a file. It takes two arguments : the name of the file and the mode in which the file should be opened. The mode can be 'r'
for reading 'w' for writing or 'a' for appending.
'''

# f = open("myfile.txt", 'r')
# Throws an error. As, file doesn't exist.

# Now , if we run it

f = open('myfile.txt','r')
text = f.read()
print(text) # It prints the content inside the .txt file.

# Modes for opening
# 'r' : Reads a file if exists , throws error if not.
# 'w' : Deletes all the data of an existing file and re-writes it, if exists , else creates a new file.
# 'a' : Opens a new file for appending without deleting the previous data , creates a new file if it doesn't exist.
# 'c' : Creates a file if doesn't exist or else throws an error.
# 'b' : Helps to handle binary files(images,pdf,etc.)


# Writing a File :
'''
To , write a file we first need to open it in write mode. We can then use the write() method to write to the file. 
'''
# Example :
m = open('myfile.txt','w')
write = m.write('Hi , this is write mode usage.')
print(text)


# Closing a File :
'''
Acche bacche file close karte hain.
'''
# Example
m.close() # Closes the file .

# Abhi with use karne se , close karne ki zaroorat nahi
with open('myfile.txt','a') as m :
    m.write("Hello")
print(m)