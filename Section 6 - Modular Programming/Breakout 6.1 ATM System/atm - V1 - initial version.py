# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Starter program for Breakout Activity 6.1 with main program and ...
# stub (dummy) functions for getting the user's choice, lodgements, and withdrawals

# A function to display the menu
def displayMenu():
    print("\t LCCS BANK LIMITED")
    print("\t ATM Main Menu")
    print("")
    print("\t(1) Balance Enquiry")
    print("\t(2) Cash Lodgement")
    print("\t(3) Cash Withdrawal")
    print("")
    print("\t(0) Exit")
    print("")    

# A function to read and valididate the menu option
def getChoice():
    return 0


# A function to process withdrawals
def processWithdrawal(withdrawalAmount):
    pass

# A function to process lodgements
def processLodgement(lodgeAmount):
    pass

# Main processing
balance = 0.0
print("Balance is %.2f" %balance)

displayMenu()
menuOption = getChoice()
while menuOption != 0:
    if menuOption == 1:
        print("Balance is %.2f" %balance)
    elif menuOption == 2:
        amount = float(input("How much do you want to lodge? "))
        processLodgement(amount)
    elif menuOption == 3:
        amount = float(input("How much do you want to withdraw? "))
        processWithdrawal(amount)

    displayMenu()
    menuOption = getChoice()


print("Thank you for banking with LCCS BANK LIMITED")
print("Balance is %.2f" %balance)



