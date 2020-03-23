# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of functions to validate data


# Version 1
# A function to keep reading until the user enters a number
def readIntegerV1():

    strN = input("Enter a number: ")
    while not strN.isdigit():
        strN = input("Enter a number: ")
        
    return int(strN)

# Version 2
# A function to keep reading until the user enters a number
def readIntegerV2():

    valid = False # valid is a Boolean variable aka a flag
    while not valid: # loop as long as valid is False 
        strN = input("Enter a number: ")
        if strN.isdigit():
            valid = True
        
    return int(strN)

# Version 3
# A function to keep reading until the user enters a number
def readIntegerV3():

    while True: # loop forever
        strN = input("Enter a number: ")
        if strN.isdigit():
            break # exit the loop
        
    return int(strN)

# Version 4
# A function to keep reading until the user enters a number
def readIntegerV4():

    while True: # loop forever
        strN = input("Enter a number: ")
        for i in range(0, len(strN)):
            if strN[i] not in "0123456789":
                break # exit the for loop
        else:
            break # exit the while loop
        
    return int(strN)

# Main Program
print(readIntegerV1())
# print(readIntegerV2())
# print(readIntegerV3())
# print(readIntegerV4())
