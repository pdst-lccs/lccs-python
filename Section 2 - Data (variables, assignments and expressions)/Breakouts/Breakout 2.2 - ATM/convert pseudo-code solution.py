# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Solution to Breakout 2.2 (ATM)

# Display a welcome message
print("Welcome to LCCS Bank Ltd.")
print("=========================")

# Initialise a variable called balance to 123.45
balance = 123.45

# Display the value of balance
print("Your balance is:", balance)

# Prompt the user to enter the amount to lodge
amount = float(input("Enter amount to lodge: "))

# Increase the balance by the amount entered
balance = balance + amount

# Display the value of balance
print("Your balance is:", balance)

# Prompt the user to enter the amount to withdraw
amount = float(input("Enter amount to withdraw: "))

# Decrease the balance by the amount entered
balance = balance - amount

# Display the value of balance
print("Your balance is:", round(balance,2) )
