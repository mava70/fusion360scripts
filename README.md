# fusion360scripts
Script for fusion 360 various automations

first script is:
changethread.py

this script automate the change of diameter of all xml files of fusion 360 defining a standard thread, in this way we can take in account of 3d print
hole downsizing, please configure the following variable in the file before run:

#how bigger os smaller (negative) holes should be in mm

tolerance_to_add=0.5

#your pc username 

username='myusername'

tolerance_to_add can be positive or negative all Thread will be increased or decreased by this amount value must be mm, in will be calculated accordingly
username is your username in the system

The script create a set of duplicated xml files of all system thread but with increased dimeter all new as "RESIZED" in the "Thread Type" name

the script is based on the following Autodesk Knowledge library:

https://knowledge.autodesk.com/support/fusion-360/learn-explore/caas/sfdcarticles/sfdcarticles/Custom-Threads-in-Fusion-360.html?_ga=2.135745329.1088301858.1676143928-1745511642.1675102800
