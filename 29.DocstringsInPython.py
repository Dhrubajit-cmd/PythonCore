# In this class we shall learn about doc-strings in python.
# And we shall also learn about PEP-8

## Docstrings in Python :
# Python docstrings are the string literals that appear right after the definition of a function,method,class or module.
# Example :
def square(n):
    '''Takes in a number n, retruns the square of n'''
    print(n**2)
square(5)

#  Here, '''Takes in a number n, returns the square of n ''' is a docstring which will not appear in output.
# Now, how is it different from the comment ?
# The difference is , docstring unlike comment is not ignored by the interpreter as it can also be printed using the following command.
print(square.__doc__)
# And another difference is , programs output can change if we change docstring, but programs output cannot be changed by changing comment.


## PEP-8 :
'''
PEP-8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum,Barry
Warsaw, and Nick Coghlan. The primary focus of PEP-8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes aspects of Python , like design
and style , for the community. 
'''

# Check this exciting thing :
import this


# Okay this is all we have got in this class .