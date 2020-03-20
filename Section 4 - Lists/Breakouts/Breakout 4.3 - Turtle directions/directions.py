# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of lists in a turtle graphic program

from turtle import *

pensize(2) # set the pen size to 2
color("red") # set the pen colour to red

# setup a list of angles
angles = [0, 90, 60, 90, 90]
# setup a list of distances
distances = [100, 75, 50, 75, 100]

left(angles[0])
forward(distances[0])
left(angles[1])
forward(distances[1])
left(angles[2])
forward(distances[2])
left(angles[3])
forward(distances[3])
left(angles[4])
forward(distances[4])

