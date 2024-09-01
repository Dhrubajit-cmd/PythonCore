# In this class we shall learn about dictionary methods in python .

# update() :
'''
The update method updates the value of the key provided to it if the item already exists in the dictionary , else it creates a new key-value
pair.
'''
ep1 = {122:45 , 123 : 89 , 124 : 69 , 670 : 69 , 165 : 45}

ep2 = {222:34,234:39,999:65}

ep1.update(ep2)
print(ep1)

# clear() :
'''
The clear method removes all the items from the list. 
'''
ep3 = {1:2 , 3:2}
ep3.clear()
print(ep3)

# pop() :
'''
The pop() mehtod removes the key-value pair whose key is passed as a parameter. 
'''
ep1.pop(122)
print(ep1)

# popitem() :
'''
The popitem() method removes the last key-value pair from the dictionary. 
'''
ep2.popitem()
print(ep2)

# del() :
'''
The del() method deletes the entire dictionary in one go.
'''
ep4 = {23:3,234:5}
#del ep4
 # print(ep4) # Throws an error.
# If key is provided then it deletes a particular key value pair:
del ep4[23]
print(ep4)

# This is all in dictionaries. But, we shall learn more along with our experience.
