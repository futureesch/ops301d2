#!/bin/bash

# Author - Tom Esch
# Last Revised - 3/3/2021
# Purpose - Automating chmod command process

###DEMO CODE###
# How to view file permissions

# ls -al

# Add file name if you want to filter the view

# ls -al testfile.txt

# How to set file permissions to a single file

# chmod 777 testfile.txt

# How to set file permissions on this directory and all its contents

# chmod -R 755 ./

# or use --recursive

# chmod --recursive 755 ./

###END OF DEMO CODE###

###Start of author code###

# Declaration of Variables


### Create a new bash script that performs the following:

# Prompts user for input directory path.
echo "Please input directory path to autochmod:"
read "answer"

# Prompts user for input permissions number (e.g. 777 to perform a 
chmod 777)

echo "Please select rwe permissions for the selected directory:"
read "numbers"

# Navigates to the directory input by the user and changes all files 
inside it to the input setting.

chmod --recursive $numbers

# Prints to the screen the directory contents and the new permissions
settings of everything in the directory.

# Ran out of energy.
