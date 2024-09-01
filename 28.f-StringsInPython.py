# In this class we shall learn about the f-strings in python.
# What is string formatting ?
# String formatting in python can be done using the format method .
# Example :
txt = "For only {price:2f} dollars!"
print(txt.format(price = 49))
# Example 2 :
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Dhrubajit"
print(letter.format(country,name))
# This is how formatting was done earlier in python.
# But now using the f string we shall see how easy it is to use .
print(f"Hey my name is {name} and I am from {country}. \n")
# See, it makes the code simple and easier.

# In order to print upto two decimal places.
price = 49.09999
txt = f"For only {price:.2f} dollars. \n"
print(txt)

print(type(f"{2 * 30}"))

# This is all about f-strings in python.

