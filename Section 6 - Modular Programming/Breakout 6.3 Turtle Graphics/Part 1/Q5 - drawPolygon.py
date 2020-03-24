# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Part I
# Q5 - solution - implement drawPolygon

from turtle import *

def drawSquare(size):
    for side in range(4):
        forward(size)
        left(90)


def drawTriangle(size):
    for side in range(3):
        forward(size)
        left(120)


def drawHexagon(size):
    for side in range(6):
        forward(size)
        left(60)

# Function to draw an n-sided polygon
# This function exploits the patterns in drawSquare, drawTriangle and drawHexagon
def drawPolygon(n, size):
    angle = 360/n
    for side in range(n):
        forward(size)
        left(angle)


# Test the function
drawPolygon(5, 200) # Draw a 5-sided polygon
drawPolygon(4, 100) # Draw a 4-sided polygon
drawPolygon(3, 50) # Draw a 3-sided polygon

