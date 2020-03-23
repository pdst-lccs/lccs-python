# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of functions to validate a Yes/No response


# Returns either Y(es) or N(o)
def readYesNoResponse():

    response = input("Enter response [Y/N]: ")
    while response != "Y" and response != "N":
         response = input("Enter response [Y/N]: ")        
    
    return response

# Test the function
print(readYesNoResponse())

# TO DO: Enhance so that 'y', Yes, and YES are also accepted
