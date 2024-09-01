# In this class we shall learn about the constructors in Python.
# Constructor objects to banane mein madad karte hain.

# Normal Tarika :
# class Person :
#     name = "Dhrubajit"
#     occ = "Developer"
#
#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a = Person()
# a.info()


# Now let us see dunder method
# The below is a parameterized constructor as this takes arguments, the other is default that does not take any argument.
class Insaan :
    def __init__(self,n,o):
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}. \n")
m = Insaan("Dhrubajit","Developer")
n = Insaan("Ashmita","Designer")
m.info()
n.info()



# Some more practice :

class Animal :
    def __init__(self,animal,group):
        self.animal = animal
        self.group = group
    def info(self):
        print(f"{self.animal} belongs to the {self.group} group.\n")
dog = Animal("Dog","Mammal")
dog.info()
crow = Animal("Crow","Birds")
crow.info()

# Let us seen an example of a default constructor :
class Naam :
    def __init__(self): # Takes no arguments so, it is a default constructor.
        print('Hey my name is Dhrubajit and I am writing a Python code. \n')
naam = Naam()
