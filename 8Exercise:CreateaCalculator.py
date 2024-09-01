print("Welcome to my basic calculator!! \n")
a = int(input(print("Enter the first number:\n")))
b = int(input(print("Enter the second number:\n")))
c = input(print("Enter the operation you want to do:\n"))
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c =='*':
    print(a*b)
elif c =='/':
    print(a/b)
elif c =='%':
    print(a%b)
elif c =='//':
    print(a//b)
elif c =='**':
    print(a**b)
else :
    print("Please enter a valid operation")
print("Thank You!!")

