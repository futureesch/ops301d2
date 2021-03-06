#!/bin/bash

# Title - Clearcutter
# Author - Tom Esch
# Last Revised - 3/6/2021
# Purpose - Clearing the contents of Log Files

# Declaration of Variables:

invar="clowns"

# How to view a file's contents

# cat /var/log/syslog
# cat /var/log/wtmp

# How to clear a file's contents

# cat /dev/null > testfile.txt

# Main 

# Menu System

while [ $invar != "0" ]
do 
  echo "Press 0 to exit."
  echo "Press 1 to show and clear syslog"
  echo "Press 2 to show and clear wtmp"
  read invar
  if [ $invar == "0" ]; then
  echo "Exiting!"
  echo "No more clearcutting for now!"
  fi 
  if [ $invar == "1" ]; then
  echo "Printing syslgo to the screen and clearing"
  cat /var/log/syslog 
  cat /dev/null > /var/log/syslog
  echo "Syslog has been clearcut!"
  fi 
  if [ $invar == "2" ]; then 
  echo "Printing wtmp to the screen and clearing"
  cat /var/log/wtmp
  cat /dev/null > /var/log/wtmp
  echo "Wtmp has been clearcut!"
  fi
done 

# End
