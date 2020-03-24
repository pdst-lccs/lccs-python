# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Part II
# Q2 - Listing B

from turtle import *

# set the appearance of the turtle
def setAppearance():
    hideturtle()
    color('red')
    pensize(5)

# Draw angle #1
def drawAngle(size):
    backward(100)
    left(size)
    forward(100)

# Position the pen
def setPenPosition():
    penup()
    setpos(200, 0)
    setheading(0)
    pendown()


# Main program starts here
setAppearance()
drawAngle(30)
setPenPosition()
drawAngle(60)




