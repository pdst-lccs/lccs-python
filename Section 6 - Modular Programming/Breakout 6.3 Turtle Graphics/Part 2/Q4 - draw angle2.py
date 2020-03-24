# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Part II
# Q4 - solution - modify drawAngle to accept co-ordinates as parameters

from turtle import *

# set the appearance of the turtle
def setAppearance():
    hideturtle()
    color('red')
    pensize(5)

# Draw angle #1
def drawAngle(x, y, size, arm1Len, arm2Len):
    setPenPosition(x, y)
    backward(arm1Len)
    left(size)
    forward(arm2Len)


# Position the pen
def setPenPosition(x, y):
    penup()
    setpos(x, y)
    setheading(0)
    pendown()


# Main program starts here
setAppearance()
drawAngle(0, 0, 30, 50, 50)
drawAngle(200, 0, 60, 100, 200)


