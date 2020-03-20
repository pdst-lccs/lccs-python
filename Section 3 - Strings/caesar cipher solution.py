# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program that shifts each letter of a 6 letter word by 1
# Example: "Python" becomes "Qzuipo".

# inStr = "Python"
inStr = input("Enter any 6 letter word: ")

outStr = chr(ord(inStr[0])+1)
outStr = outStr + chr(ord(inStr[1])+1)
outStr = outStr + chr(ord(inStr[2])+1)
outStr = outStr + chr(ord(inStr[3])+1)
outStr = outStr + chr(ord(inStr[4])+1)
outStr = outStr + chr(ord(inStr[5])+1)

print(outStr)
