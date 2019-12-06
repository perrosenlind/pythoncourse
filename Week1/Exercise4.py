#!/usr/bin/env python3
# Exercise 3 on Python for network engineers.

'''
4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 


Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.

'''


#initiate variable
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "


#remove trailing and leading space
#show_version = show_version.strip()

model = show_version.split()[1]

serial = show_version.split()[2]

#Check if Cisco is contained in the model sting
print()

if 'cisco' in model.lower():
    print("It's a Cisco device!")

if '881' in model:
    print ("This is a 800-series router")


#Print Serial table with info
print()
print("{:^15}{:^15}".format("Model", "Serial"))
print("-" * (2 * 15))
print("{:^15}{:^15}".format(model, serial))

#Alternative solution printout:
print()
print()
print("Serial number: {}".format(serial))
print("Model: {}".format(model))

     





