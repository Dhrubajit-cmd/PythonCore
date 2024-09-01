# In this class we shall learn about while loops in Python and its uses.

# Let us take a sample code using the for loop .
for i in range(3):
    print(i)

# We can do the same thing using while as done below :
m = 0
while (m < 3):
    print(m)
    m = m + 1
# You see same things can be done using while and for.So, this means that both of them are same.
# But in some cases the use of for becomes easy whereas in some place use of while becomes easy.

# While loop is generally used in complex programs where we take input from users.
# Sample Code :
k = 0
while(k<=40) :
    k = int(input("Enter the number : \n"))
    print(k)
# This code keeps on taking input from the user until the user enters a value greater than 40 .

# So, what is while loop ?
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes false,the
# interpreter comes out of the loop.


## Else with While Loop :
# We can even use the else statement wiht the while loop. Essentially what the else statement does is that as soon as the while loop
# condition becomes false, the interpreter comes out of the while loop and the else statement is executed.
count = 5
while (count > 0) :
    print(count)
    count = count - 1
else :
    print("I am inside else now.")

# A simple implementation of else with while loop :
str = "NAMOINDIA"
passwd = input("Enter your password: \n")
while (passwd != str):
  print("Incorrect password \n")
  passwd = input("Enter your password: \n")
else:
  print("Hello Dhrubajit ! \n")

# Emulate do while loop in python :
while True :
    print(i)
    i = i +1
    if (i%100 == 0) :
       break
# This emulates the do while loop

# Let's try one more :
numpass = "Hello"
while True :
    tap = input(print("Enter your password: \n"))
    if tap == numpass :
        break

# This is also an example