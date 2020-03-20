# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people
# Version: 2.0 

# A program to calculate the average height of 5 people
print("Average height calculator")
print("=========================")

# Read in the 5 values
totalHeight = 0

height = float(input("Enter height (cm): "))
totalHeight = totalHeight + height
height = float(input("Enter height (cm): "))
totalHeight = totalHeight + height
height = float(input("Enter height (cm): "))
totalHeight = totalHeight + height
height = float(input("Enter height (cm): "))
totalHeight = totalHeight + height
height = float(input("Enter height (cm): "))
totalHeight = totalHeight + height

# Calculate the average
avgHeigth = totalHeight/5

# Display the result
print("The average height is", round(avgHeigth,2), "cm")
print("The average height is "+str(round(avgHeigth,2))+"cm")
