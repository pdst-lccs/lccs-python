# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q2
# Purpose: A program to find the GCD of any two positive integers


# Determines if one number is a factor of the other
def isFactor(a1, a2):
    if a2 % a1 == 0:
        return True
    else:
        return False

# Returns a list containing all the factors of n
def getFactors(n):
    factors = []
    for i in range(1, n+1):
        if isFactor(i, n):
            factors.append(i)
    return factors        

# Returns the greatest common divisor
# This is the largest number that is common to both lists
def gcd(l1, l2):
    # sets don't contain duplicates
    set1 = set(l1)
    set2 = set(l2)
    common_factors = set1.intersection(set2) # set1 & set2
    return(max(common_factors))
    

# Main program
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

list_of_factors1 = getFactors(n1)
list_of_factors2 = getFactors(n2)
ans = gcd(list_of_factors1, list_of_factors2)
print("The GCD of %d and %d is %d" %(n1, n2, ans))


'''
# Alternative solution
def gcd(a, b):
    while b:
        a, b = b, a % b
   
    print(a)

gcd(27, 63)
'''
