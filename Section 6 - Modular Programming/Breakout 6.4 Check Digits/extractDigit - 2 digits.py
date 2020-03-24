# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits
# Extract the digits from a 2 digit number


n = int(input("Enter a 2 digit number: "))
d2 = n%10       # %10 extracts the final digit
d1 = n//10      # //10 to remove the final digit
print(d1, d2)
