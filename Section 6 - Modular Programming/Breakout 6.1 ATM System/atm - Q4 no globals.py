# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Solution to Breakout Activity 6.1 - suggested activities (Modifications)
# ATM System
# Menu driven program handle balance enquiries, lodgements, and withdrawals
# Q4 - No global variables

# A function to display the menu
def displayMenu():
    print("\t LCCS BANK LIMITED")
    print("\t ATM Main Menu")
    print("")
    print("\t(1) Balance Enquiry")
    print("\t(2) Cash Lodgement")
    print("\t(3) Cash Withdrawal")
    print("\t(4) Change PIN")
    print("")
    print("\t(0) Exit")
    print("")    

# A function to read and valididate the menu option
def getChoice():
    
    validChoice = False
    while not validChoice:
        choice = input("\t CHOOSE AN OPTION >> ")                
        if choice.isdigit():
            choice = int(choice)
            if (choice >= 0) and (choice <= 4):
                validChoice = True

    return choice


# A function to process withdrawals
def processWithdrawal(bal, withdrawalAmount):
    #global balance

    # Q1. Prevent withdrawals exceeding €200
    if withdrawalAmount > 200:
        print("The maximum withdrawal amount permitted is €200")
        return

    if (withdrawalAmount > bal):
        print("Insufficient Funds.")
    else:
        bal = bal - withdrawalAmount
        print("Please take your cash.")

    return bal

# A function to process lodgements
def processLodgement(bal, lodgeAmount):
    # global balance

    if (lodgeAmount%10 == 0):
        bal = bal + lodgeAmount
    else:
        print("Amounts must be a multiple of 10.")

    return bal


# A function to read the balance from the file
def readATMFile():
    # global balance, pin
    global pin
    
    bankFile = open("atm.txt", "r")
    bal = float(bankFile.readline())
    pin = int(bankFile.readline())
    bankFile.close()
    return bal

# A function to write balance to the file
def writeATMFile(bal):
    global pin
    
    with open('atm.txt', 'w') as bankFile:
        bankFile.write(str(bal))
        bankFile.write("\n")
        bankFile.write(str(pin))

# This function returns a valid PIN
def getValidPIN(msg):

    validPIN = False
    
    while not validPIN:
        userPin = input(msg)
        if userPin.isdigit():
            userPin = int(userPin)
            if (userPin >= 0) and (userPin <= 9999):
                validPIN = True
    # is 12 a vaid PIN
    return userPin


# This function returns TRUE if the PIN entered matches the system PIN
# FALSE otherwise.
def isValidUser(currentPin):

    userPin = -1
    tries   =  0
    while ((userPin != currentPin) and (tries < 3)):
        userPin = getValidPIN("Enter your 4 digit PIN >> ")
        tries  =  tries+1

    if (userPin == currentPin):
        return True
    else:
        return False


# This function returns TRUE if the user PIN was entered correctly. FALSE otherwise.
def changePin(oldPin):

    newPin1 = getValidPIN("Enter your new 4 digit PIN >> ")
    newPin2 = getValidPIN("Confirm your new 4 digit PIN >> ")    

    if (newPin1 == newPin2):
        return newPin1
    else:
        print("PIN mistmatch - change unsuccessful")
        return oldPin


# Main processing
pin = 0000
# Q2 Add a line to read atm.txt
balance = readATMFile()

if isValidUser(pin):
    displayMenu()
    menuOption = getChoice()
    while menuOption != 0:
        if menuOption == 1:
            print("Balance is: %.2f" %balance)
        elif menuOption == 2:
            amount = float(input("How much do you want to lodge? "))
            balance = processLodgement(balance, amount)
        elif menuOption == 3:
            amount = float(input("How much do you want to withdraw? "))
            balance = processWithdrawal(balance, amount)
        elif menuOption == 4:
            pin = changePin(pin)

        displayMenu()
        menuOption = getChoice()

    writeATMFile(balance)
    print("Thank you for banking with LCCS BANK LIMITED")
    print("Balance is: %.2f" %balance)
else:
    print("Invalid PIN. Access denied")
