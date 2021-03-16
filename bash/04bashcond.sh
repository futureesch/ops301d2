#!/bin/bash

# Author - Tom Esch
# Last Revised - 3/16/2021
# Purpose - Bash conditional statements

#Create a bash script that launches a menu system with the following
options:
  #Hello world (prints “Hello world!” to the screen)
  #Ping self (pings this computer’s loopback address)
  #IP info (print the network adapter information for this computer)
  #Exit

#Next, the user input should be requested.

#The program should next use a conditional statement to evaluate the
user’s input, then act according to what the user selected.

#Use a loop to bring up the menu again after the request has been 
executed.

# Declaration of Variables:

invar="clowns"

# Menu System

while [ $invar != "0" ]
do 
  echo "Press 1 to display Hello World!"
  echo "Press 2 to ping self"
  echo "Press 3 to display ip configuration info"
  echo "Press 0 to exit"
  read invar
  if [ $invar == "0" ]; then
  echo "Exiting!"
  fi 
  if [ $invar == "1" ]; then
  echo "Hello World, I am your OVERLOAD-LORD!"
  fi 
  if [ $invar == "2" ]; then 
  echo "Pinging this computer"
  ping 127.0.0.1 
  fi
  if [ $invar == "3" ]; then
  echo "Displaying ip configuration information"
  ip a 
  fi 
done 

# Fin
