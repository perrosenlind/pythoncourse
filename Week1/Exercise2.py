#!/usr/bin/env python3
# Exercise 2 on Python for network engineers.

'''
2. Prompt a user to enter in an IP address from standard input. 
Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​ $ python exercise2.py 
Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------


Four columns, fifteen characters wide, a header column, data centered in the column.
'''

#Ask for an ip address
ip_addr = input('Please enter an IP address: ')


#split ip address into octects
octets = ip_addr.split('.')

#print out the ip address based with one octect per column
#The star tells you to treat the items in the list as individual items in a sequence.

#Draw the outline of the layout
print()
print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet 1", "Octet 2", "Octet 3", "Octet 4"))
print("-" * (4 * 15))

#Print in decimal
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))

#print in binary
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))

#print in hex
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))

#Print end border
print("-" * (4 * 15))
print()
print()


