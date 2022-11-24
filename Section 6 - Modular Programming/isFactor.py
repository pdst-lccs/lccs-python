# Event: LCCS Python Fundamental Skills Workshop
# Date: No 2022
# Author: Sinead Crotty, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate boolean functions

# A function to determine if one number, n2 is a factor of another number, n1.
def isFactorV1(n1, n2):
    if n1%n2 == 0:
        return True
    else:
        return False

def isFactorV2(n1, n2):
    return n1%n2 == 0

# print(isFactorV1(6,3))
# print(isFactorV1(5,3))
# 
# print(isFactorV2(6,3))
# print(isFactorV2(5,3))
