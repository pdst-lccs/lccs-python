# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the str command
# The running total is displayed in a formatted string

# Program to calculate a running total

# Initialise the variable
runningTotal = 0

# Perform the calculations
price1 = float(input("Enter the 1st price: "))
runningTotal = runningTotal + price1
price2 = float(input("Enter the 2nd price: "))
runningTotal = runningTotal + price2
price3 = float(input("Enter the 3rd price: "))
runningTotal = runningTotal + price3

# Display the output
print("Total amount is €%s" %str(runningTotal))

