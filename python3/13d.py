#!/usr/bin/env python3
# Author - Tom Esch
# Last Revised - 03/17/2021
# Purpose - Requests

import requests

# Prompt the user to type a string input as the variable for your 
destination URL.

def main():

#Prompt the user to select a HTTP Method of the following options:

choice = '0'
while choice =='0':
    print("what would you like to do with" + site)
    print("Select 1 for get")
    print("Select 2 for post")
    print("Select 3 for put")
    print("Select 4 for delete")
    print("Select 5 for head")
    print("Select 6 for patch")
    print("Select 7 for options")

    choice = input

    if choice == "1":
        requests.get(site), data={'key':'value'}) 
    elif choice == "2":
        requests.post(site), data={'key':'value'})
    elif choice == "3":
        requests.put(site)
    elif choice == "4":
        requests.delete(site)
    elif choice == "5":
        requests.head(site) 
    elif choice == "6":
        requests.patch(site), data={'key':'value'}) 
    elif choice == "7":
        requests.options(site) 
    else:
        print ("That is not an option")

main()

#Print to the screen the entire request your script is about to send
Ask the user to confirm before proceeding.

#Using the requests library, perform a GET request against your lab 
web server.

#For the given header, translate the codes into plain terms that pri
to the screen; for example, a ‘404’ error should print ‘Site not 
found’ to the terminal instead of ‘404’.

#For the given URL, print response header information to the screen.
