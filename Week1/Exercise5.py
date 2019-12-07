#!/usr/bin/env python3
# Exercise 3 on Python for network engineers.

'''

5. You have the following three variables from the arp table of a router:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS" mappings. The output should look like following:

             IP ADDR          MAC ADDRESS
-------------------- --------------------
        10.220.88.29       5254.abbe.5b7b
        10.220.88.30       5254.ab71.e119
        10.220.88.32       5254.abc7.26aa


Two columns, 20 characters wide, data right aligned, a header column.
'''

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#build table layout
print()
print()
print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20}{:>20}".format(("-" * 19 ), ("-" * 19)))

#Print the ip and mac in the right column
print("{:>20}{:>20}".format(mac1.split()[1], mac1.split()[3]))
print("{:>20}{:>20}".format(mac2.split()[1], mac2.split()[3]))
print("{:>20}{:>20}".format(mac3.split()[1], mac3.split()[3]))