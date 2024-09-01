# In this class we shall learn about the Lambda Function in Python.
'''
In Python , a lambda function is a small anonymous function without a name.It is defined using the lambda keyword and has the following syntax :
lambda arguments : expression
Lambda functions are often used in situations where a small function is required for a short period of time . They are commonly used as arguments to higher-order functions , such as, map , filter
and reduce.

The below is an example of how to use a lambda function :
'''

# Function to double the input :
def double(x):
    return x * 2
print(double(5))
# Lambda function to double the input :
dokarna = lambda x: x * 2
print(dokarna(6))

# Similarly agar main cube a function banau toh :
cube = lambda x: x*x*x
print(cube(3))
'''
The above lambda function had the same functionality as the double function defined earlier. However, the lambda function is anonymous , as it does not have a name . 

Lambda functions can have multiple arguments , just like regular functions . Here is an example of a lambda function with multiple arguments :
'''
avg = lambda x,y,z:(x+y+z)/3
print(avg(5,3,10))
