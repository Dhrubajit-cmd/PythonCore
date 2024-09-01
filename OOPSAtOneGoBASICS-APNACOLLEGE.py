# In this class we shall learn about OOP in Python.


class Student:
  college_name = "ABC College"
  name = "Anonymous"
  # Isi ko constructor kaha jata hain.
  # Default Constructor
  def __init__(self):
    print("This is non parameterized constructor.")
  # Parameterized Constructor
  def __init__(self,name): # Class ke andar jo data save hote hain unhe attributes kaha jata hain.
    # print(self)
    self.name = name
  def show(self):
    print(f"The name is {self.name}. \n")
  def welcome(self):
      print('Welcome Student. \n')

s1 = Student("Rohan")
s1.show()
s2 = Student("Karan")
s2.show()
print(Student.college_name)
print(s1.name)
s1.welcome()
# Clearly OOP makes it quite easier than the procedural programming.
# OOP is a way of thinking and writing code.


# Attributes :
# Attributes are the variables that are associated with an object. {Yani koi bhi variable/data}
# Two types :
# Class.attr :- Sari objects ke liye common .
# Instance Attribute :- Yani har object ke liye alag.
# Remember , Obj Attribute > Class Attribute.

class Baccha :
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
  @staticmethod # Decorator  # They makes the function run at the class level.
  def hello():
    print("Hello. \n")
  @staticmethod
  def thankyou():
    print("Thank You.\n")
  def avg(self):
    sum = 0
    for value in self.marks :
      sum = sum + value
    print(f"Hi, {self.name} your average score is {sum/3}.\n")
b1 = Baccha("Aditya", [87,76,98])
b1.hello()
b1.avg()
b1.thankyou()




# IMPORTANT
# Abstraction :
# Hiding the implementation details of a class and only showing the essential features to the user.
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False
  def start(self):
    self.clutch = True
    self.acc = True
    print("Car Started. \n")
car1 = Car()
car1.start()
# This is called abstraction , yahan toh koi unnecessary implementation details nahi hai.

# Encapsulation :
# Wrapping data and functions into a single unit(object).
# Jo hum ab tak karte aaye hain that is all encapsulation.

# del keyword :
class Delkey :
  def __init__(self,name):
    self.name = name

s1 = Delkey("Shraddha \n")
print(s1.name) # Shows it
del s1.name
# print(s1.name) # Throws error as the del keyword deletes the attribute name.

# Private(like) attributes and methods :
# Conceptual Implementation :
'''
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.
'''
class Account :
  def __init__(self,acc_no,acc_pass):
    self.acc_no = acc_no
    self.__acc_pass = acc_pass # Do underscore lagake private kar sakte hain.
  def reset_pass(self): # Proper way to access the private thing (attribute)
    print(self.__acc_pass) # Class ke andaar use kar sakte hain.

acc1 = Account("12345","abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass) # Cannot be accessed directly
# print(acc1._Account__acc_pass) # Can be accessed indirectly . This is also called name mangling in python.
print(acc1.reset_pass()) # However, this is the best way to access it.


# Inheritance :
'''
When one class(child/derived) derives the properties & methods of another class(parent/base).
'''

class Car :
  @staticmethod
  def start():
    print("Car Started. \n")

  @staticmethod
  def stop():
    print("Car Stopped. \n")

class ToyotaCar(Car):
  def __init__(self,name):
    self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
car1.start()

# Three types of inheritance :
# Single Level Inheritance : Single Parent class aur usse ek single derived class nikalti hain.
# Multi-Level Inheritance : Parent class aur usse ek derived class aur usse ek aur derived class.
# Multiple Inheritance :  Agar ek derived class hain toh yeh multiple classes ki properties ko derive kar sakti hain.

class A :
  varA = "Welcome to class A"
class B :
  varB = 'Welcome to class B'
class C(A,B) :
  varC = "Welcome to class C "

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
'''
Super Method 
'''
# Super method :
# super() method is used to access methods of the parent class.

class Gaadi :
  def __init__(self,type):
    self.type = type
  @staticmethod
  def start():
    print('Car Started. \n')
  @staticmethod
  def neutral() :
    print("Car is Neutral.\n")
  @staticmethod
  def stop():
    print('Car Stopped. \n')
class MarutiCar(Gaadi) :
  def __init__(self,name,type):
    self.name = name
    super().__init__(type)
    super().neutral()

car1 = MarutiCar("Baleno","Electric")
print(car1.type)

# Class Method :
# A class method is bound to the class and recieves the class as an implicit first argument.
# Note :- static method can't access or modify the class state and are generally used for utility.

class Basic :
  name = "Anonymous"
  @classmethod
  def changename(cls,name):
    cls.name = name


p1 = Basic()
p1.changename("Rohan")
print(p1.name)
print(Basic.name)

# Property decorator :
# We use @property decorator on any method in the class to use the method as a property.
class Chatra :
  def __init__(self,phy,chem,math):
    self.phy = phy
    self.chem = chem
    self.math = math
  @property
  def percentage(self):
    return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Chatra(98,96,95)
print(stu1.percentage)

stu1.phy = 76
print(stu1.percentage)


# Polymrophism :
# When the same operator is allowed to have different meaning according to the context.
# For example, in mathematics, addition and subtraction are the same operator.
# But in programming, addition and subtraction are two different operators.

class Complex :
  def __init__(self,real,img):
    self.real = real
    self.img = img
  def showNumber(self) :
    print(self.real,"+",self.img,"i")

  def __add__(self,num2) :
    newReal = self.real + num2.real
    newImg = self.img + num2.img
    return Complex(newReal,newImg)
  def __sub__(self,num2):
    newReal = self.real - num2.real
    newImg = self.img - num2.img
    return Complex(newReal,newImg)

num1 = Complex(3,5)
num1.showNumber()

num2 = Complex(5,7)
num2.showNumber()

num3  = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()