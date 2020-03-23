# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q6 (b)
# Purpose: A program to display the dates of Easter Sunday between 2010 and 2030

# Returns the correct ordinal suffix for num (attached to num)
def ordinal( num ):

    suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

    if num % 100 in (11,12,13):
        s = 'th'
    else:
        s = suffix[num % 10]

    return str(num) + s

def toEasterMonth(mm):
    if mm == 3:
        return 'March'
    elif mm == 4:
        return 'April'        

def getEaster(year):

    # Step 1
    b = year // 100
    c = year % 100
    
    # Step 2    
    a = (5*b+c) % 19
    
    # Step 3    
    r = (3*(b+25)) // 4
    s = (3*(b+25)) % 4

    # Step 4    
    t = (8*(b+11)) // 25        
    # Step 5
    h = (19*a+r-t) % 30
    # Step 6    
    g = (a+11*h) // 319
    # Step 7    
    j = (60*(5-s)+c) // 4
    k = (60*(5-s)+c) % 4
    # Step 8    
    m = (2*j-k-h+g) % 7
    # Step 9    
    n = (h-g+m+110) // 30
    q = (h-g+m+110) % 30

    # Step 10    
    p = (q+5-n) % 32

    dStr = ordinal(p)
    mStr = toEasterMonth(n)
    yStr = str(year)
    return dStr+" "+mStr+" "+yStr

'''
# A more concise implementation of getEaster()
def calc_easter2(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    #print("a=%d b=%d c=%d d=%d e=%d f=%d" %(a, b, c, d, e, f))
    month = f // 31
    day = f % 31 + 1    
    return year, month, day
'''

# Main program
for yr in range(2000,2031):
    print(getEaster(yr))