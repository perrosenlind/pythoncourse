#!/usr/bin/env python3
# Exercise 1 on Python for network engineers.

"""
3. Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)


Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
"""

from pprint import pprint


#Read the file
with open("show_arp.txt") as show_arp:
    list_arp = show_arp.readlines()

#Remove the header of the list with a list slice:
list_arp_noheader = list_arp[1:]

#print the list using pretty print
pprint(list_arp_noheader)


#Sort the list based on ip addresses
list_arp_noheader.sort()

#grab the first three addresses 
first_three = list_arp_noheader[:3]

#use .join () to add first_three to the string with '\n' as the separator
first_three = '\n'.join(first_three)

#Print first_three to file
with open("arp_entries.txt", "wt") as output:
    output.write(first_three)