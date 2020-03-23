# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q5
# Purpose: A program to display a date (assumed to be valid) entered as
# dd, mm, yyyy in the (long) format d, mmm, yyyy


# Returns the correct ordinal suffix for num (attached to num)
def ordinal( num ):

    suffix = ['th', 'st', 'nd',
              'rd', 'th', 'th',
              'th', 'th', 'th', 'th']

    if num % 100 in (11,12,13):
        s = 'th'
    else:
        s = suffix[num % 10]

    return str(num) + s

def get_month_name(m):
    monthNames = ['Jan', 'Feb', 'Mar',
                  'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep',
                  'Oct', 'Nov', 'Dec']
   
    return monthNames[m-1]

# Read a valid number
def get_number(prompt):
    while True:
        strN = input(prompt)
        if strN.isdigit():
            break
        
    return int(strN)    


# Main program
dd = get_number("Enter day (dd): ")
mm = get_number("Enter month (mm): ")
yyyy = get_number("Enter year (yyyy): ")

# We will assume a valid date
ddStr = ordinal(dd)
mmStr = get_month_name(mm)

print("Long date %s %s %d" %(ddStr, mmStr, yyyy))