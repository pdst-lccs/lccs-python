# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits
# Extract the digits from a 4 digit number

n = int(input("Enter a 4 digit number: "))
d1 = n%10         # %10 extracts the final digit
d2 = (n//10)%10   # //10 chops off the last digit
d3 = (n//100)%10  # //100 chops off the last two digits
d4 = (n//1000)%10 # //1000 chops off the last three digits
print(d1, d2, d3, d4)

