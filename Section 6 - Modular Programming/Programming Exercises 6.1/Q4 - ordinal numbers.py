# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q4
# Purpose: A program to display the ordinal value of a number

# Returns the correct ordinal suffix for num (attached to num)
def ordinal( num ):

    suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

    if num % 100 in (11,12,13):
        s = 'th'
    else:
        s = suffix[num % 10]

    return str(num) + s

# Read a valid number
def get_number():
    while True:
        strN = input("Enter a number: ")
        if strN.isdigit():
            break
        
    return int(strN)    


# Main program
number = get_number()
print(ordinal(number))
