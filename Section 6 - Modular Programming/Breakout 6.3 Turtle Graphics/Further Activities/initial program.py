# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Further Activities
# Q1 - initial code

from turtle import *

def drawShape1():
    for i in range(6):
        forward(50)
        left(60)

def drawShape2():
    right(60)
    for i in range(3):
        forward(50)
        left(60)
    forward(100)        
    left(120)
    forward(100)
        
def drawShape3():
    right(60)
    for i in range(3):
        forward(50)
        left(60)
    left(60)
    forward(100)
    
def drawShape4():
    right(60)
    for i in range(3):
        forward(50)
        left(60)


hideturtle()
# Insert your code under here ...
setheading(0)
drawShape1()
#drawShape2()
#drawShape3()
#drawShape4()


