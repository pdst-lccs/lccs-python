# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate simple interest

# Ask the user for the principal
principal = input("Enter principal: ")
principal = float(principal)

# Ask the user for the interest rate
rate = input("Enter rate: ")
rate = float(rate)

# Ask the user for the length of time
time = input("Enter time in years: ")
time = float(time)

# Simple interest calculation
amount = principal * rate * time

# Display the answer
print("The interest amount is", amount)
