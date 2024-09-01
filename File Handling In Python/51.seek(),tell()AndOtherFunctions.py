# In this class we shall learn about seek() , tell() and other functions in File Handling in Python.
'''
In python , the seek() and tell() functions are used to work with the file objects and their positions within a file. These functions are part of the built-in io module, which provides a
consistent interface for reading and writing to various file-like objects , such as files , pipes and in-memory buffers.
'''
# Now let's talk about the seek() function :
'''
The seek() function allows you to move the current position within a file to a specific point . The position is specified in bytes, and you can mov either forward or backward from the current 
position . For example : 
'''
with open('file.txt','r') as f :
    # Move to the 10th byte in the file
     f.seek(10) # Matlab, 'Yaar jump karke jao.' .
    # Read the next 5 bytes
     data = f.read(10)
     print(data)

# Now let's talk about the tell() function :
'''
The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative 
to the current position. For example :
'''
with open('file.txt','r') as f :
    f.read(20)
    current_position = f.tell() # Tells us what the current position of the cursor.
    print(current_position)
    f.seek(current_position) # We have seek() or shifted the cursor at the position revealed by tell().
    print(f.read()) # We have read after that .

# Now let's talk about the truncate() function :
'''
When you open a file in Python using the open function,you can specify the mode  in which you want to open the file . If you specify the mode as 'w' or 'a', the file is opened in write mode and
you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.
Here, is an example of it :
'''
with open('file.txt','a') as f :
    f.truncate(10) # Matlab, maine yeh bol diya ki mere file mein sirf 10 characters hone cahiye toh isne usko rakha aur baaki ko mita diya.
with open('file.txt','r') as f :
    print(f.read())
