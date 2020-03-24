# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.3 Turtle Graphics - Further Activities
# Q2 - initial code

from turtle import *

def movePenTo(x, y):
    penup()
    setpos(x, y)
    pendown() 

def drawVertLineUp():
    setheading(90)
    forward(50)

def drawVertLineDown():
    setheading(270)
    forward(50)

def drawHorizLineRight():
    movePenTo(xcor()+5, ycor())
    setheading(0)
    forward(50)
    movePenTo(xcor()+5, ycor())    

def drawHorizLineLeft():
    movePenTo(xcor()-5, ycor())
    setheading(180)
    forward(50)
    movePenTo(xcor()-5, ycor())

hideturtle()
# Insert your code under here ...


