#!/usr/bin/env python3
# Exercise 1 on Python for network engineers.

"""
1. Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. Print out the file contents to the screen. 
Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). 
Read in the file contents using the .readlines() method. Print out the file contents to the screen. 
Also print out the type of the variable (you should have a list at this point).
"""

#open the file
my_version = open("show_version.txt")

#read the file
show_version = my_version.read()

#print the file to the screen
print(show_version)

#close the file after use.
my_version.close()

#do the same again, with python context manager
with open("show_version.txt") as show_version:
    output = show_version.read()

print(output)

