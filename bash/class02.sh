#!/bin/bash

# Author - Tom Esch
# Last Revised - 3/2/2021
# Purpose - Copy syslog to a file in the current directory and time stamp it

# Variables

year=`date +%Y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
echo `date`
echo "Current Date: $day-$month-$year"
echo "Current Time: $hour:$minute:$second"

# Prints the file to screen and makes a file

echo "Original file before append:"
cat /var/log/syslog > syslog

# The >> double carrot here will row append
# Time appended to the created file "syslog"

echo "Current Date and Time: $day-$month-$year $hour:$minute:$second"  
>> syslog
echo "Appended file:"
cat syslog
