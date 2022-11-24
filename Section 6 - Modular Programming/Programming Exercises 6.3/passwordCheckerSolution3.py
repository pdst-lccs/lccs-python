# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Sinead Crotty, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q4
# Purpose: A program to validate a password
# A valid password is one which is ....
# a) between 9 and 12 characters in length and
# b) contains only uppercase letters/lowercase letters/digits/symbols

# A function that returns True if 'p' is a valid password. False otherwise
def isValidPassword(p):
    
    if (len(p) < 9) or (len(p) > 12):
        return False
    
    symbols = "_+-*/!?&^@"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    
    # Concatenate the 4 strings into a single string of allowed characters
    allowed_chars = symbols + upper_case_letters + lower_case_letters + digits
    
    # Loop through each 'char' in 'p' to check validity
    for char in p:
        if char not in allowed_chars:
            return False
        
    # The loop has ended so the password must be valid - return True
    return True    


# Main program starts here
password = input("Enter a password: ")
if isValidPassword(password):
    print("%s is a valid password" %password)
else:
    print("%s is an invalid password" %password)
