# In this class we shall learn about a part of OOP, Classes and Objects in Python .

class Person :
    name = "Harry"
    age  = 44
    occupation = "Software Developer"
    salary = "160K"
    def info(self):
        print(f"{self.name} is a {self.occupation}.His/Her salary is {self.salary}.")
a = Person()
a.name = "Dhrubajit"
# print(a.name,",", a.occupation)
a.info()
'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. 
It must be provided as the extra parameter inside the method definition. 
'''
# Yani woh object jis par yeh method call ho rha hain.

# Agar main aisa karu toh :
b = Person()
b.name = "Nitika"
b.occupation = "HR"
b.salary = "200K"
b.info()

# Done next class mein aur complex seekhenge.