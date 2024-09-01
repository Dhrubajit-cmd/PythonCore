# In this class we shall learn about how import works in python.
'''
Importing in Python is the process of loading code from a Python module into the current script . This allows
you to use the functions and variables defined in the module in your current script , as well as any additional mdules
that the imported module may depend on .
To import a module in Python , you use the import statement followed by the name of the module. For example, to import
the math module which contains a variety of mathematical functions, you would use the following statements.
import math

Once a module is imported you can use any of the functions and variables defined in the module by using the dot notation .
For example, to use the sqrt function from the math module, you would write the following :
'''
import math
result = math.sqrt(9)
print(result)


'''
You  can also import specific functions or variables from a module using the from keyword. 
Example :
'''
from math import sqrt
res = sqrt(144)
print(res)

# OR
from math import pi
print(pi)

# Importing Everything :
'''
It's also possible to import all functions and variables from a module using the * wildcard. 
However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific 
functions and variables are coming from . 

'''
# Remember this is not recommended it can make our code slower and less effective.
from math import *
print(sqrt(169))
print(pi)

# The use of as :
from math import sqrt as sqr # You can make the thing you are importing easy to call by giving it the simple names using as.
print(sqr(100))

# The dir function :
'''
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables 
defined in a module. This can be helpful for exploring and understanding the contents of a new module.
'''
# Example
import math
print(dir(math))

import pandas
print(dir(pandas))

# This is all about the import in python.