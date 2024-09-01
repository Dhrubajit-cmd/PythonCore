# readlines() method :
'''
readlines() method reads a single line from the file. If we want to read multiple lines we can use a loop.

'''

f = open('myfile.txt','r')
while True :
    line = f.readline()
    print(line)
    if not line :
        break
# The above command helps us to readlines in the myfile.txt

# Now let us do something more amazing :
file = open('file.txt','w')
# i = 0
# while True :
#   i = i + 1
#   k = file.readline()
#   if not k :
#       break
#   m1 = k.split(',')[0]
#   m2 = k.split(',')[1]
#   m3 = k.split(',')[2]
#   print(f"Marks of Maths of student {i} is {m1}. \n")
#   print(f"Marks of English of student {i} is {m3}. \n")
#   print(f"Marks of Social Science of student {i} is {m3}. \n")



# writelines() Method :
'''
This code helps us writelines in a file .Let us see its example use :
'''
lines = ['line1\n','line2\n','line3\n']
file.writelines(lines)
file.close()