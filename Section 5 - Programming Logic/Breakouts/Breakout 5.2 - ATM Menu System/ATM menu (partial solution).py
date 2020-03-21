# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A partial solution to Breakout 5.2 ATM Menu System

print("\t|-------------------------------|")
print("\t|\t LCCS BANK LIMITED\t|")
print("\t|\t ATM Main Menu\t\t|")
print("\t|\t\t\t\t|")
print("\t|\t1. Balance Enquiry\t|")
print("\t|\t2. Cash Lodgement\t|")
print("\t|\t3. Cash Withdrawal\t|")
print("\t|\t4. Cash Transfer\t|")
print("\t|\t5. Change PIN\t\t|")
print("\t|\t6. Other Services\t|")
print("\t|\t\t\t\t|")
print("\t|\t7. Exit\t\t\t|")
print("\t|-------------------------------|")
print("\t|\t\t\t\t|")
print("\t| CHOOSE AN OPTION >> \t\t|")
print("\t|\t\t\t\t|")
print("\t|-------------------------------|")
print("")


option = input("Enter an option between 1 and 7: ")
# Validate. Ensure the option entered is within the correct data range
while option not in ("1", "2", "3", "4", "5", "6", "7"):
   option = input("Enter an option between 1 and 7: ")

option = int(option) # convert the option to an integer

# Initialise the balance
balance = 0
if option == 1:
    print("Current Balance is €%d" %balance)
elif option == 2:
    amount = float(input("Enter an amount to lodge: "))
    balance = balance + amount
    print("Current Balance is €%d" %balance)

# The rest is left as an exercise ....

print("Goodbye. Thank you")



