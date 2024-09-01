'''
Question :
Create a python project that opens an application as per user's wish if his/her correct name and password is entered.
'''

import os
print("Welcome. \n")
name = input("Enter your name: \n")
if name == "Dhrubajit Chakravarty" :
    passwd = input("Enter your password: \n")
    password = "dc2006"
    if passwd == password :
        list = ["1.Browser","2.Storage","3.Email","4.Quit"]
        print(list)
        value = int(input("Enter the value for the app you want to open: \n"))
        if value == 1 :
            os.system("firefox")
        elif value == 2 :
            os.system("gparted")
        elif value == 3 :
            os.system("thunderbird")
        elif value == 4 :
            print("Thank you for using our services. \n")
        else :
            raise ValueError(print("Invalid Input. \n"))
    else :
        raise ValueError(print("Enter the correct password. \n"))
else :
    raise ValueError(print("Enter the correct name. \n"))
