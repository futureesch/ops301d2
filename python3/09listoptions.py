#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 3/11/2021
# Purpose - Proto Data Science Script

# Assign to a variable a list of ten string elements.

thislist = ["ibanez", "dean", "squier", "rivolta", "sidejack",
"cordoba", "pbass", "uke", "alvarez", "gretsch"]

# Main

# Print the fourth element of the list.

print(thislist[3])

# Print the sixth through tenth element of the list.

print(thislist[5:])

# Change the value of the seventh element to “onion”.
# This site helped - https://datatofish.com/modify-list-python

thislist[6] = "onion"
print(thislist)

#Fin

