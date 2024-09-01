# Object Introspection :
# dir() dict() aur help() methods and how to use it when we deal with new classes.

#  They make it easy for us to understand how classes resolve various and executes code.

# dir() helps us to see all the methods along with the dunders of a class that we mention to it.
x = [1,2,3]
print(dir(x))
print(x.__add__)

y = (1,2,3)
print(dir(y))


# dict() method converts the self.any = data into dictionary with key as any and value as data. Like do in the example below.
class Person :
    def __init__(self,name,age:int):
        self.name = name
        self.age = age
        self.version = 1
    # @staticmethod
    # def call():
    #     print("Welcome Brother. \n")

p = Person("Dhruabjit",18)
print(p.__dict__)

n = Person("Harry",20)
print(n.__dict__)


# help() generally ek class ya cheez ke bare mein sab kuch batata hain.

print(help(str))