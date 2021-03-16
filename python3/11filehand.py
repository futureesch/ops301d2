#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 3/15/2021
# Purpose - File Handling

# Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

f = open("demofile.txt", "w+")

for i in range(3):
     f.write("This is line %d\r\n" % (i+1))

f.close()

f = open("demofile.txt", "r")
line = f.readline()
print(line)
f.close()

import os
os.remove("demofile.txt")

#Fin
