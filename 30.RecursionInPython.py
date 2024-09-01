# In this class we shall talk about Recursion in Python.
# It means calling the same function inside the function .
# Let us use it to get the factorial of the numbers :
# def factorial(n) :
#     if (n==0 or n ==1):
#         return 1
#     else :
#         return n * factorial(n-1)
# print(factorial(4))
# This is called recursion

def factorial_9():
    ''' This function consecutively prints the factorial of the numbers from 1 to 10. '''
    def factorial(n) :
        '''
        This function defines the factorial of the numbers other than 0 and 1
        '''
        if (n == 1):
            return 1
        else :
            return n * factorial(n-1)
    k = int(input("Enter the number upto which you want it's factorial to get printed: \n"))
    for i in range(1,k+1):
       if (i ==1) :
           factorial1 = 1
           print(factorial1)
       else :
           factorial1 = factorial(i)
           print(factorial1)
print(factorial_9())

# This is the advanced used of recursion .


# Another popular use is calculation of Fibonacci Series.
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(n-1) + f(n-2)

# Let's write the program :
# Function to print fibonacci series till the user wants.
def fibonacci(n) :
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_6():
    m = int(input("Enter the number upto which you want the Fibonacci series to get printed: \n"))
    for i in range(0,m+1):
        if (i == 0) :
            ans = 0
            print(ans)
        elif (i == 1) :
            ans = 1
            print(ans)
        else :
            ans = fibonacci(i)
            print(ans)
fibonacci_6()





