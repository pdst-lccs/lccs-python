# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Sinead Crotty, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q4
# Purpose: A program to validate a password
# A valid password is one which is ....
# a) between 9 and 12 characters in length and
# b) contains only uppercase letters/lowercase letters/digits/symbols

# A function the returns True if 'userPassword' is a valid password. False otherwise
def checkLength(word):
    if 9 <= len(word) <= 12:
        return True
    else:
        return False

def checkChars(password):
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "_+-*/!?&@^"
    acceptableChars = lower_case_letters + upper_case_letters + digits + symbols
    result = True
    for i in range(len(password)):
        if password[i] not in acceptableChars:
            result = False
    return result

def isValid(passwordToCheck):
    lenOkay = checkLength(passwordToCheck)
    charsOkay = checkChars(passwordToCheck)
    return lenOkay and charsOkay
    
userPassword = input("Enter your password here >>>")
if isValid(userPassword):
    print("Valid password")
else:
    print("Invalid password")
