# ATM v2
# Menu driven program handle balance enuiries, lodgements, and withdrawals


# A function to display the menu
#def displayMenu():
#    pass

# A function to read and valididate the menu option
def getChoice():
    return 0


# A function to process withdrawals
def processWithdrawal(withdrawalAmount):
    return

# A function to process lodgements
def processLodgement(lodgeAmount):
    return

# Main processing
balance = 0.0
print("Balance is %.2f" %balance)
print("1")
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

    print("2")
    
print("Thank you for banking with LCCS BANK LIMITED")
print("Balance is %.2f" %balance)


