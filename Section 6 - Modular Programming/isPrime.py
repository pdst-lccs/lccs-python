# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to display all the prime numbers up to 100

import math

# A function to test whether a number is prime or not
# Returns True if the number is prime; False otherwise
def isPrime(numToCheck):

    # Any number less than 2 is not prime
    if numToCheck < 2:
        return False

    # see if num is evenly divisible by any number up to num/2
    divisor = 2
    while (divisor <= numToCheck/2):
        if (numToCheck % divisor == 0):
            return False
        divisor = divisor+1

    # The number must be prime so return True
    return True


# Test harness
for num in range(100):
    if (isPrime(num)):
        print(num, "is prime")
