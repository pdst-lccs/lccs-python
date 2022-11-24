# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate function composition

def sub(a, b):
    answer = a - b
    return answer

print(sub(4, 3)) # 1
print(sub(3, 4)) # -1
print(sub(3, -4)) # 7

# print( sub( 2, sub(3, 4))) # -> displays 3
# print( sub( sub(2, 3), 4)) # -> displays -5
# print( sub( 2, sub(3, sub(4, 5)))) # -> displays -2

# Predict what the print statements below would display
# Now uncomment the lines and run the code
# print( sub( 5, 1))
# print( sub( 1, 5))
# print( sub( 2, sub(4, 3)))
# print( sub( 1, sub(2, sub(3, 4))))

# Were your predictions correct?
