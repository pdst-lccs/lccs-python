# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2023
# Author: Computer Science, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people
# Version: Q4 - this version allows decimal values for heights

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
