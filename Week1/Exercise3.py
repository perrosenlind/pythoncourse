#!/usr/bin/env python3
# Exercise 3 on Python for network engineers.

'''
3.   
Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. 
The second variable should use all upper case characters with underscore as the word separator. 
The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

ip_addr = "2001:db8:1234::1"
IP_ADDRESS = "2001:db8:1234::2"
Ip_Adress3 = "2001:db8:1234::3"

print(ip_addr == IP_ADDRESS)
print(ip_addr != Ip_Adress3)