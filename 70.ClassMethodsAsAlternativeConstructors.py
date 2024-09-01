class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    def fromutc(cls,string):
        return cls(string.split("_")[0],string.split("_")[1])

e = Employee("Harry",12000)


string = "John-120000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)

# string = "Jonny_13000"
# e3 = Employee.fromutc(string)
# print(e3.name)
# print(e3.salary)

# Baaki Practice ke saath seekhoge
