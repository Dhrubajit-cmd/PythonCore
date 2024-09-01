# In this class we shall study about Sets in Python.
# What are Sets in Python ?
# Sets are generally a collection of well defined objects.
s = {2,4,2,6}
print(s)
# You will see that if won't print the repeated value.
# Remember, set doesn't follow any order.
#So, a proper definition would be :
'''
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed 
within curly brackets{}. Sets are unchangeable , meaning you cannot change items of the set once created. Sets,do not contain duplicate items. 
'''
# Example :
info = {False, "Carla",45, True, 63}
print(info)
# Wrong code to create an empty set :
seta = {}
print(type(seta))
# As, you shall see that the type of seta is an empty dictionary.
# Correct Code to create an empty set.
harry = set()
print(type(harry))

# You can access the set items in this way, i.e. using for loop.  :
for value in info :
    print(value)

