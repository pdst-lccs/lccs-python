# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Part I
# Q3 - solution - implement drawSquare(dimension)

from turtle import *

# A function to draw a square
def drawSquare(dimension):
    forward(dimension)
    right(90)
    forward(dimension)
    right(90)
    forward(dimension)
    right(90)
    forward(dimension)
    right(90)
    
# Call the function
drawSquare(100)


