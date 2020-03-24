# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Part I
# Q4 - solution - implement drawRectangle(dimension, dimension)

from turtle import *

# A function to draw a rectangle
def drawRectangle(width, height):
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)

# A function to draw a square
# This function exploits the fact that a square is a special kind of rectangle ...
# ... i.e. a square is a rectangle with 4 sides of equal dimensions
def drawSquare(dimension):
    drawRectangle(dimension, dimension)


# Call the function
drawSquare(100)



