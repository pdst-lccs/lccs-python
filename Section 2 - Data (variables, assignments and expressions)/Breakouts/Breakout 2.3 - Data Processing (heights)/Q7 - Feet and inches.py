# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Computer Science, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people
# Version: Q7 - this version displays the result in feet and inches as well as centimetres

print("Average height calculator")
print("=========================")

# Read in the 5 values
h1 = float(input("Enter first height (cm): "))
h2 = float(input("Enter second height (cm): "))
h3 = float(input("Enter third height (cm): "))
h4 = float(input("Enter fourth height (cm): "))
h5 = float(input("Enter fifth height (cm): "))

# Calculate the average height
avgHeigth = (h1+h2+h3+h4+h5)/5

# Display the result
print("The average height is ", round(avgHeigth,2), "cm")
print("The average height is ", round(avgHeigth*0.393701,2), "inches")
