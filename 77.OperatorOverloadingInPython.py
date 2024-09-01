# In this class we shall learn about Operator Overloading in Python.

# This is only called Operator Overloading in Python.

class Complex :
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    def showNumber(self):
        print(f"{self.real} + {self.imaginary}i")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImaginary = self.imaginary + num2.imaginary
        return Complex(newReal,newImaginary)
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImaginary = self.imaginary - num2.imaginary
        return Complex(newReal,newImaginary)

num1 = Complex(3,4)
num2 = Complex(4,8)
num1.showNumber()
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()

num5 = num3 + num4
num5.showNumber()
