# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people
# Version: 1.0 (This program contains deliberate errors)

print("Average height calculator")
print("=========================")

# Read in the 5 values
h1 = int(input("Enter first height (cm): "))
h2 = int(input("Enter second height (cm): "))
h3 = int(input("Enter third height (cm): "))
h4 = int(input("Enter fourth height (cm): "))
h5 = int(input("Enter fifth height (cm): "))

# Calculate the average height
avgHeigth = h1+h2+h3+h4+h3/5

# Display the result
print("The average height is ", avgHeigth, "cm")
