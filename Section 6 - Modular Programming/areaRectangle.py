# Event: LCCS Python Fundamental Skills Workshop
# Date: Nov 2022
# Author: Sinead Crotty, PDST
# eMail: computerscience@pdst.ie
# Name: AreaRectangle.py
# Purpose: A program to calculate the area of a rectangle

def calc_area_rect(length, width):
    area = length * width
    print("The area of the rectangle is",area)
    
calc_area_rect(4,3)

"""
# Alternative solution
def calcArea(length, width):
    area = (length*width)
    print("The area is ", area, "cm squared")


l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
calcArea(l,w)
"""
