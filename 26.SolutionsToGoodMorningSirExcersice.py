import time
# timestamp = time.strftime("%H")
hour = int(time.strftime('%H'))
if hour >= 0 and hour < 12 :
    print("Good Morning Sir. \n")
elif hour >= 12 and hour < 16 :
    print("Good Afternoon Sir. \n")
elif hour >= 16 and hour < 24 :
    print("Good Evening Sir. \n")
log = input("Do you want to log-out now ? \n")
if log == "Yes" or log == "yes" :
    print("Good Night Sir. \n")
else :
    print("Okay \n")

# This is the solution to the Good Morning Sir Question.
# For further more please join me in the course .

