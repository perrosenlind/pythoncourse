#!/usr/bin/env python3
# Exercise 1 on Python for network engineers.

"""
5. Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
"""

#read the file
with open("show_ip_bgp_summ.txt") as f:
    bgp_summary = f.read()

#split the file into different lines
bgp_summary = bgp_summary.splitlines()

#get the as number from the last value on the first row
local_as = bgp_summary[0].split()[-1]

#get the bgp peer from the last line
bgp_peer = bgp_summary[-1].split()[0]

#Print bgp peer ip and as number
print('BGP Peer IP Address: ' ,bgp_peer, ' with AS number: ' ,local_as)

