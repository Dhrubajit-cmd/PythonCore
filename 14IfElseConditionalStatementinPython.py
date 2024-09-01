# Here, we shall learn about the if else statement in python.
# Let us see a simple use of this if-else statement.

# It takes user input of his age and confirms whether the user can drive or not.
# welcome = "Welcome to Driving Eligibility"
# print(welcome.center(200,"."))
# a = int(input("Enter your age: \n"))
# print(f"Your age is {a} \n")
# if a >= 18:
#     print("Yes you can drive. \n")
#     print("You will be redirected to a page to enter your personal details. \n")
# else :
#     print("Sorry you are not eligible to drive.")
# bye = "Thank you"
# print(bye.center(200,"."))


# Now let's take an implementation of elif statement:
apple = 210
banana = 180
budget = int(input("Enter your budget: \n"))
if budget >= apple:
    print(f"Your budget is {budget}.So, you can buy either apple or banana.")
    choice = ["1.Apple","2.Banana"]
    print(choice)
    choose = int(input("Enter your choice,what do you wanna buy? : \n"))
    if choose == 1 :
        print(f"Okay!! As per your choice {choose}. Buying 1kg of Apples.... \n ")
        m = budget - apple
        left = print(f"Bought!! You are left out with {m} rupees. \n")
        if m >= banana:
            print("Do you want to buy banana ? \n")
            c = ["1. Yes", "2. No"]
            print(c)
            chm = int(input("Enter your choice: \n"))
            if chm == 1:
                print("Okay buying bananas.... \n")
            elif chm == 2:
                print("Okay discarding.... \n")
            else:
                print("Please enter a valid input!! \n")
        elif m < banana:
            print(f"You are left out with {m}. \n")
    elif choose == 2:
        print(f"Okay!! As per your choice {choose}. Buying 1kg of Bananas.... \n")
        n = budget - banana
        bacha = print(f"Bought!! You are left out with {n} rupees. \n")
        if n >= apple:
            print("Do you want to buy apples ? \n")
            d = ["1. Yes", "2. No"]
            print(d)
            dhm = int(input("Enter your choice: \n"))
            if dhm == 1:
                print("Okay buying apples.... \n")
            elif dhm == 2:
                print("Okay discarding.... \n")
            else:
                print("Please enter a valid input!! \n")
        elif n < apple:
            print(f"You are left out with {n}. \n")
    else :
        print("Please enter a valid input!! \n")
elif budget == banana :
    print(f"As per your budget which is {budget}. Buying 1kg of bananas.... \n")
elif budget > banana :
    print(f"As per your budget which is {budget}. Buying 1kg of bananas.... \n")
elif budget < banana :
    print(f"As per your budget which is {budget}, you cannot buy banana!!! \n")
else :
    print("Please enter a valid input!!! \n")

# This command takes the user input of their budget and returns whether they are to buy banana or apple.








