# There are four types of arguements that we can provide in a function.
# 1. Default Arguement.
# 2. Keyword Arguement.
# 3. Variable Length Arguements.
# 4. Required Arguements.

## Default Arguements :
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the
# function call for that argument.
# Example :
def name(fname, mname = "John",lname = "Whatson"):
    print("Hello",fname,mname,lname)
name("Amy") # If you see here, you shall notice that we have added some default values to the function while defining it . And then we call the
# fucntion by giving "Amy" as the fname.
# Let's check another example :
def day(tday , tmday = "Tuesday",wday = "Wednusday"):
    print(f"Today is {tday}, tomorrow shall be {tmday}, the day after tomorrow shall be {wday}")
day("Monday") # This is another example of default arguments.
# OR
def average(a=5,b=9) :
    print("The average is",(a+b)/2)

average() # This is also an example here, we have defined the default values of a and b right in the definition of the function .
# But if we call the function this way
average(8,9)
# Then it shall ignore the default values and carry out the function using the values defined by the user.
average(b=12)
# This keeps a as default but changes the value of b to 12
# Similarly this change can also be carried out with a .

## Keyword Arguments :
# We can provide arguments with key = value , this way the interpreter recognizes the arguments by the parameter name.Hence, the order in which
# the arguments are passed does not matter.
# Example :
def naam (fname , mname , lname):
    print("Hello",fname,mname,lname)
naam(fname = "Anil",lname = "Raju", mname = "Dhanush") # See,the order in which we entered the key = value doestn't matter it recogizes the name of
# the parameter.

## Required Arguments :
# In case we don't pass the arguments with a key = value syntax , then it is necessary to pass the arguments in the correct positional order and the
# number of arguments passed should match with actual function definition.
# Example :
def naa (fname , mname , lname):
    print("Hello",fname,mname,lname)
naa("Nikhil","Ashutosh","Naman")

## Variable Length Argument :
# Sometimes we may need to pass more arguments than those defined in the actual function . This can be done using variable length arguments.

# There are two ways to achieve this :
 # Arbitary Arguments :
 # While creating a function pass a * before the parameter name while defining the function . The function accesses the arguments by processing them
 # in the form of tuple .
 # Example :
def naas(*name):
     print("Hello",name[0],name[1],name[2])
naas("James","Wilton","Barness")

# Let's see another example of it :
def averagea(*numbers):
    sum = 0
    for i in numbers :
        sum = sum + i
        print("The average of the numbers is :",(sum)/len(numbers))
averagea(23,34,45,69,85)

 # Keyword Arbitary Arguments :
 # While creating a function pass a ** before the parameter name while defining the function. The function accesses the arguments
 # by processing them in the form of dictionary .

  # Let's see an example of it :
def namas(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
namas(fname = "Dhrubajit",mname = "Harbajan",lname = "Sampat")

## Return Statement :
# Let us directly see its use
def returnname (fname, lname , mname):
    return  \
        (print("Hello",fname,lname,mname))
c = returnname("ram","anant","shambhu")
print(c)
