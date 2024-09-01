class Employee :
    def __init__(self,name):
      self.name = name
    def __len__(self): # Magic Methods.
        return len(self.name)
    def __str__(self):
         return f"The name of the employee is {self.name}. \n"

    def __repr__(self):
        return f"Hello {self.name}. \n"
    def __call__(self):
        print('hey I am good \n')
e = Employee("Dhrubajit")

print(e)
print(len(e))
print(str(e))
print(repr(e))
e()