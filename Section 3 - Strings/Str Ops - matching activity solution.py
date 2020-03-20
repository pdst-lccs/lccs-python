# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: String Operation Activity

# Initialise the string
alNum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#                  1         2         3         4         5         6
#        01234567890123456789012345678901234567890123456789012345678901

print(alNum[3])     # "d"
print(alNum[52:62]) # "0123456789"
print(alNum[51:62]) # "Z0123456789"
print(alNum[26:53]) # "ABCDEFGHIJKLMNOPQRSTUVWXYZ0"
print(alNum[0:25])  # "abcdefghijklmnopqrstuvwxy"
print(alNum[1])     # "b"
print(alNum[5])     # "f"
print(alNum[26:52]) # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alNum[26])    # "A"

# END OF SOLUTION

# The code below could be used for another question
# (Just remove the triple quotes to activate)
'''
print("")
print(alNum[52])    # "0"
print(alNum[25:52]) # "zABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alNum[2])     # "c"
print(alNum[0:26])  # "abcdefghijklmnopqrstuvwxyz"
print(alNum[51:61]) # "Z012345678"
print(alNum[6])     # "g"
print(alNum[25])    # "z"
print(alNum[51])    # "Z"
print(alNum[0])     # "a"

# A general pattern used to find the last character
print( alNum[len(alNum) - 1] ) # "0"
'''
