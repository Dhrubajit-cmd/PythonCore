# Question :
'''
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code
language.
Coding :
if the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end.
else :
  simply reverse the string
Decoding:
if th word contains less than 3 characters , reverse it
else :
 remove 3 random characters from start and end.Now, remove the last letter and append it to the beginning.
'''

# Solution :
import random
import string
# Main stream question to the user :
intro = "R.A.W"
intro_centre = intro.center(200,".")
print(intro_centre)
while True :
  decision_list = ["1.Code","2.Decode","3.Quit"]
  print(decision_list)
  decision = int(input("Enter what you want to do : \n"))
  if decision == 1:
# Coding :
    def generate_random_string(length=3):
    # Generate a string of 'length' random letters
     random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))
     return random_string
    str = input("Enter the word you want to code: \n")
    def append_str() :     
     k = str[1:]
     x = str[0]
     append = k + x
     return append
    m = generate_random_string()
    n = generate_random_string()
    coded_str = m + append_str() + n
    print(coded_str)
  elif decision == 2:
# Decoding :
   str_coded = input("Enter the str that is coded: \n")
   str_primary = str_coded[3:-3]
   final = str_primary[-1] + str_primary[0:-1]
   print(final)

  elif decision == 3:
     break

  else :
     print("Enter a valid input. \n")

print("Thank you for using our services.  \n")
extro_center = intro.center(200,'.')
print(extro_center)
