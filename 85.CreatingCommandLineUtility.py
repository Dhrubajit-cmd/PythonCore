# In this class mein hum log command line utility ko banana seekhenge.

# What is Command Line Utility ?
'''
Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python,
we can create our own Command Line Utility using the built-in argparse module .
'''

# importing required modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description = "An addition program")

# add argument
parser.add_argument("add", nargs = '*', metavar = "num", type = int, help = "All the numbers separated by spaces will be added.")

# parse the arguments from standard input
args = parser.parse_args()

# check if add argument has any input data.
# If it has, then print sum of the given numbers
if len(args.add) != 0:
	print(sum(args.add))

# We shall learn it later. After finishing the course.


