#!/usr/bin/env python3
# Exercise 1 on Python for network engineers.

"""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
"""

#Create a list with 5 ip address
ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4", "10.1.1.5"]

#use append to add an ip address to the end of the list.
ip_list.append("10.1.2.3")

#use extend to add two more addresses
ip_list.extend(['192.168.1.1' , '192.168.1.2'])

#Use list concatenation to add two more IP addresses to the end of the list.
ip_list = ip_list + ['172.16.1.1' , '172.16.1.2']

#print out the list of addresses
print(ip_list)

#print out the first address in the list
print("First ip address in the list. " + ip_list[0])

#print out the last ip address in the list
print("Last ip address in the list: " + ip_list[-1])

#remove the first and list ip in the list
first_ip = ip_list.pop(0)
last_ip = ip_list.pop()

#Update/Overwrite the first Ip adress to 2.2.2.2
ip_list[0] = '2.2.2.2'

print("New first ip: " + ip_list[0])
