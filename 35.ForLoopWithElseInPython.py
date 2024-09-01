# In this class we shall learn for Loop with else in Python.
# Simple example :
for i in range(1,10) :
    print(i)
else :
    print("Go. \n")

# OR
list = [1,3,4,5,6]
for i in list :
    print(f"The thing is {i}. \n")
else :
    print("Sorry. \n")

# A QUIZ
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i.")
'''
Remember, else will not get executed. Else, execute hone ka matlab hain ki loop break nahi hua , loop khatam hua hain. Par yahan loop break hua
hain isiliye excute nahi hoga. 
'''


# Similarly with while :
i = 0
while i < 7 :
    i = i + 1
    print(i)
    if i == 4 :
        break
else :
    print("Sorry no i. \n")
# Yahan bhi nahi hoga

i = 0
while i < 7 :
    i = i + 1
    print(i)
else :
    print("Sorry no i. \n")
# Abh hoga!!.

# This is all about else with for and while loop.
