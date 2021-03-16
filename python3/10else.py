#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 3/15/2021
# Purpose - Else

# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = input("Enter the first value: ")
b = input("Enter the second value: ")

if a == b:
    print("The first value is equal to the second value.")
if a != b:
    print("The first value is NOT equal to the second value.")
    if a < b: 
        print("The first value is also less than the second value. ")
    elif a <= b:
        print("The first value is less than or equal to the second 
value.")
    if a > b: 
        print("The first value is also greater than the second value.
")   
    elif a >= b:
        print("The first value is greater than or equal to the second
")     
              
# Fin




