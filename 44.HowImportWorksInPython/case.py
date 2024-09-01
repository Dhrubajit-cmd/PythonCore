import time
def welcome() :
    hour = int(time.strftime("%H"))
    if hour >= 0 and hour < 12 :
       print("Good Morning \n")
    elif hour >= 12 and hour < 16 :
       print("Good Afternoon \n")
    elif hour >= 16 and hour < 24 :
       print("Good Evening \n")
    config = input("Do you want to log out ? \n")
    if config == "yes" or config == "Yes":
       print("Have a nice day. \n")
    else :
       print("Okay \n")


