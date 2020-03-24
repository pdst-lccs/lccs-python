# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits
# Extract the digits from a 3 digit number

n = int(input("Enter a 3 digit number: "))
d1 = n%10         # %10 to extract the final digit
d2 = (n//10)%10   # //10 to remove the final digit
d3 = (n//100)  # //100 to remove the final two digits
print(d1, d2, d3)
