#!/usr/bin/env python3

# Author - Tom Esch
# Last Revised - 3/16/2021
# Purpose Using 

# Time spent by processes executing in kernel mode
# Time when system was idle
# Time spent by priority processes executing in user mode
# Time spent waiting for I/O to complete.
# Time spent for servicing hardware interrupts
# Time spent for servicing software interrupts
# Time spent by other operating systems running in a virtualized 
environment
# Time spent running a virtual CPU for guest operating systems un
the control of the Linux kernel

import psutil

print(psutil.cpu_times(), file=open("output.txt", "a"))

# Fin
