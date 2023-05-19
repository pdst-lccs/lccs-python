# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2023
# Author: Computer Science, PDST
# eMail: computerscience@pdst.ie
# Purpose: Turtle Graphics - Further Activities
# Python Manual, page 17, Further Activites - Exercise 3

from turtle import * # import the turtle graphics library

#draws a 50 x 50 square
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)

#draws a 50 x 100 red rectangle
# color("red") # set the pen colour to red
# forward(50)
# left(90)
# forward(100)
# left(90)
# forward(50)
# left(90)
# forward(100)

#draws a vertical blue line of length 100 units and thickness 5 units
# color("blue")
# pensize(5)
# left(90)
# forward(100)

#draws the letter 'T' in red - pen is hidden
color("red")
left(90)
forward(100)
left(90)
forward(50)
left(180)
forward(100)
hideturtle()
