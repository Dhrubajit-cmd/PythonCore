# Joining Sets :
'''
Sets in python more or less work in the same way as sets in mathematics.We can perform operations like union and intersection
on the sets just like in mathematics.
'''

# 1 . union() and update() :
'''
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas
update() method adds item into the existing set from another set. 
'''
# Union :
name = {"Dhrubajit","Hanamo","Clerk","Stuwart"}
cities = {"India","Japan","America","United Kingdom"}
name_cities = name.union(cities)
print(name_cities)
# OR
s1 = {1,2,3,4}
s2 = {4,5,6,7}
s3 = s1.union(s2)
print(s3)
# Update :
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)

# 2. intersection() and intersection_update() :
'''
The intersection() and intersection_update() methods prints only items that are similar to both the sets.The intersection() method returns a new set whereas
intersection_update() method updates into the existing set from another set. 
'''
# intersection() :
m1 = {2,4,5,7,8,9}
m2 = {2,7,5,97,199}
m3 = m1.intersection(m2)
print(m3)
 # This creates a new set that is basically the intersection of the two  existing sets.

# intersection_update :
ma1 = {3,45,65,33,4,6,7}
ma2 = {23,3,4,556,6,89,7}
# Change the ma1 by filling up with intersected  values.
ma1.intersection_update(ma2)
print(ma1)
# Changes the ma2 by filling up with intersected values.
ma2.intersection_update(ma1)
print(ma2)


# 3. symmetric_difference and symmetric_difference_update :
'''
The symmetic_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() mehtod returns a 
new set whereas symmetric_difference_update() method updates into the existing set from another set. 
'''
# symmetric_difference() :
mas1 = {2,4,6,89,900,345,67}
mas2 = {2,4,89,678,4356,677,98}
mas3 = mas1.symmetric_difference(mas2)
print(mas3)
# This creates a new set with numbers having symmetric difference in mas1 and mas2.

# symmetric_difference_update() :
# This updates the mas1 with symmetric difference between mas1 and mas2.
mas1.symmetric_difference_update(mas2)
print(mas1)
# This update the mas2 with symmetric difference between mas1 and nas2.
mas2.symmetric_difference_update(mas1)
print(mas2)

# 4. isdisjoint() :
'''
The isdisjoint() method checks if items of given set are present in another set.This method returns False if items are present, else it
returns True.
'''
# If not disjoint then returns False.
dis1 = {1,3,4,67,7,34,54}
dis2 = {1,3,54,4,7,5667,67}
print(dis1.isdisjoint(dis2))
# If disjoint sets then returns True.
dis3 = {1,2,3,4,5,6}
dis4 = {7,8,9,10,11}
print(dis3.isdisjoint(dis4))

# 5. difference() and difference_update() :
'''
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. 
The difference() method returns a new set whereas, difference_update() method updates into the existing set from another set.  
'''
# difference() :
# Generally A-B
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
# That is , the numbers which are in A but not in B
res = set2.difference(set1)
print(res) # Output : {5,6}
# That is, the numbers which are in B but not in A

# difference_update() :
set1.difference_update(set2)
print(set1)
# Changes the set 1 with the elements of A-B
# Similar can be done with the set2.

# issuperset() :
'''
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are
present, else it returns False.
'''
ss = {1,2,3,4,5}
ss2 = {1,2,3,4,5,6,7,8}
print(ss2.issuperset(ss)) # True as ss2 is superset of ss
print(ss.issuperset(ss2)) # False as all values of ss is not in ss2 , or ss is not superset of ss2.
# Verification of Maths :
print(ss.issuperset(ss)) # True , Maths Verified.

# issubset() :
'''
The issubset() method checks if all the  original set are present in the particular set. It returns True if all the  items are present, else 
it returns False.
'''
print(ss.issubset(ss2)) # True
print(ss2.issubset(ss)) # False , As, ss2 is the superset not subset.
# Verification of Maths :
print(ss2.issubset(ss2)) # True , Maths Verified.

# add() :
'''
If you want to add a single item to the set use the add() method. 
'''
# Example :
mn = {1,2,3,4,5}
print(mn)
mn.add(6)
print(mn)

# remove() :
'''
Used to remove elements from the set. 
'''
mn.remove(4)
print(mn)

# discard() :
'''
Used to remove elements from the set. 
'''
mn.discard(3)
print(mn)

'''
The main difference between the discard() and remove() is, if we remove an non-existing element from the set it raises an error. 
Whereas, if we discard a non-existing element from the set it do not raise any error. 
'''
# Example :
# Now element 4 is not in set :
# Using remove :
#mn.remove(4) # This shall raise an error. As, evident.
#print(mn)
# Using discard :
mn.discard(4) # This will not raise an error. As, evident.
print(mn)

# pop() :
'''
This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered. 
However, you can access the popped item if you assign the pop() method to a variable. 
'''
mass = {1,2,3,4,56,7}
mass.pop()
print(mass)
# See we don't know what will be removed as, sets are unordered.

# del :
'''
Deletes the entire set. 
'''
cits = {"Ajmer","Delhi","Guwahati","Namrup"}
del cits
print(cits) # Error as cits is remove.

# That is all in sets.
# Bye Bye