# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate iterative and recursive computations of factorial


# A recursive solution to factorial
def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

# An iterative solution to factorial
def factorial(n):
    
    answer = 1
    for i in range(n, 1, -1): 
        answer = answer * i
    
    return answer

# Test the function 
x = 5
print("%d! = %d" %(x, factorial(5)))

