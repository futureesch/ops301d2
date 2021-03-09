#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 3/8/2021
# Purpose - Running a bash script from inside python3

# To run a bash script inside python3
# = https://stackoverflow.com/questions/13745648/
running-bash-script-from-within-python

# Calling the bash script and running it
#import subprocess
# subprocess.call("./computerinfo.sh", shell=True)
# Didn't work for me, but down the way 

# But this did! This is the second time my trip to stack overflow has
been a solution down low... so I give my up vote.
import os
os.system('bash computerinfo.sh')

# computerinfo.sh

#!/bin/bash

# Script: BashGrep.sh                       
# Author: Tom Esch                      
# Date of latest revision: February 2nd, 2021     
# Purpose: 
    # regular expressions - REGX
    # grep [options] searchwordpattern [./randomfile.txt] like ctrl
+find, except it will return the entire line for the pattern 
TARGETS STORAGE
    # helps to dig through log files
    # ip a to grep enp0s3 requires a "pipe" | (like a baton in a relay)
    # piped: operation | grep pattern TARGETS MEMORY
    # i/o | i/o
    # > sends to directory in hand with a .txt or something
    # sudo lshw

# https://unix.stackexchange.com/questions/363004/
how-to-grep-two-lines-from-lshw

# https://www.networkworld.com/article/3583598/
how-to-view-information-on-your-linux-devices-with-lshw.html

# https://www.howtoforge.com/linux-lshw-command/

# Declaration of Variables
ComputerName="This is the name computer:"
BIOSinfo="BIOS information:" 
cpuinfo="System CPU information:" 
raminfo="System RAM information:"
displayadapterinfo="Display Adapter information:"
networkadapterinfo="Network Adapter information:"

# Ram description, physical ID, Size

# Display adapter description, product, vendor, physical ID, Bus info, Width, Clock, Capabilities, Configuration, Resources

# Network adapter description, product, vendor, physical ID, Bus info, logical name, version, serial, size, capacity

# Use grep to remove irrelevant info

# Add text to the out clearl indicating which component the script is returning info about

# Run as root

# Main

echo $ComputerName

sudo lshw -short -sanitize | grep system 

echo $cpuinfo 

sudo lshw | grep -A 5 cpu | head -n6 

echo $raminfo 

sudo lshw | grep -A 5 memory | head -n4

echo $displayadapterinfo 

sudo lshw | grep -A 12 display | head -n12

echo $networkadapterinfo

sudo lshw | grep -A 11 network | head -n11

echo "All done, budday!"

# End
