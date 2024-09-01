# In this class we shall learn about Getters and Setters in Python.
class MyClass :
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}. \n")
    @property # This is called Getter
    def ten_value(self):
        return 10* self._value

    @ten_value.setter # This is called Setter
    def ten_value(self,new_value):
        self._value = new_value/10
obj = MyClass(100)
obj.show()
obj.ten_value = 67
print(obj.ten_value)
obj.show()

# Simple Example :
class Student:
    def __init(self):
        print("This is a non parameterized/default constructor. \n")
    # Parameterized Constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def show(self):
        print(f"The name of the student is {self.name} the marks scored is {self.marks}. \n")

s1 = Student("Karan",89)
s2 = Student("Riya",97)
s1.show()
s2.show()


# I shall learn it later based on the requirement.