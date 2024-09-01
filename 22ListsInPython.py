# In this class we shall learn about lists in python .
l = [2,4,5]
# This is a list.
print(type(l)) # As you can see after running this program .
print(l[0])
print(l[0:2])
# This append adds a new value to the end of the list
m = l.append(6)
print(l)
# Remove command helps to remove the desired value from the strings.
m = l.remove(6)
print(l)
m = l.remove(2)
print(l)

# Now let us see negative index :
print(l[-2])
# See, simple !!!


list = [3,4,5,"Dhrubajit",True]
if "Dhrubajit" in list :
    print(True)
else :
    print(False)
if "naman" in list :
    print(True)
else :
    print(False)

# Do the same thing apply in strings . Answer is , Yes !!
# Let's see an example :
h = "Harry"
if "Ha" in h :
    print(True)
else :
    print(False)
# OR
if "Ha" in "Harry" :
    print(True)
else :
    print(False)
# Even this is correct.

## Now, let us see about the JUMP INDEX
print(list[1:4:2])
# Here 1 is starting it shall end at 3 , here it shall take the step 2 as 2 is mentioned i.e. skip one number in between.

## Let us now learn about list comprehension .
# List comprehension are used for creating new lists from other iterables like lists , tuples , dictionaries , sets and even in arrays and strings.
# Example 1 :
lst = [i for i in range(8)]
print(lst)
names = ["Hariram" , "Raju" , "Oman", "Obonirno","Sukhoya","Onupriya"]
listm = [i for i in names if "o" in i]
print(listm)
lista = [i for i in names if "R" in i]
print(lista)
listas = [naam for naam in names if "Ha" in naam]
print(listas)
# You see simple.
lm = [i*i for i in range(10)]
print(lm)
ls = [i**i for i in range(10) if i%2 == 0]
print(ls)
# See this is also possible .So, these are all with lists.
# Next Class - Lists Methods.
