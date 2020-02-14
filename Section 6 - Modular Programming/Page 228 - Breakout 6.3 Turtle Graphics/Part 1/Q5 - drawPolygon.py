# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of turtle graphics
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


def drawPolygon(sides, size):
    angle = 360/sides
    for side in range(sides):
        forward(size)
        left(angle)


drawPolygon(5, 100)

