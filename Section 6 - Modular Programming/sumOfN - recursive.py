# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate recursion

# A recursive function to add up the first n numbers. 
# Example: The sum of the first 5 numbers is 5 + the sum of the first 4 numbers
# So, the sum of the first n numbers is n + the sum of the first n-1 numbers
def sumOfN(n):
    
    if n == 0:
        return 0
    
    return n + sumOfN(n-1)

# Call the function to test it
answer = sumOfN(5)
print(answer)
