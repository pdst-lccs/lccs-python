'''
# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate function composition
'''

def sub(a, b):
    answer = a - b
    return answer

print( sub( 2, sub(3, 4)))
print( sub( sub(2, 3), 4))
print( sub( 2, sub(3, sub(4, 5))))


#print( sub( 2, sub(3, 4)))
#print( sub( 2, sub(3, sub(4, 5))))