# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate splitlines

# Notice the use of triple quotes to create a string that spans multiple lines
seussStr = """I do not like green eggs and ham.
I do not like them Sam-I-am.
I do not like them here or there.
I do not like them anywhere.
I do not like them in a house
I do not like them with  a mouse"""
bList = seussStr.splitlines()
print(bList)

'''
# Version 2 - does the exact same thing as above
line1 = "I do not like green eggs and ham.\n"
line2 = "I do not like them Sam-I-am.\n"
line3 = "I do not like them here or there.\n"
line4 = "I do not like them anywhere.\n"
line5 = "I do not like them in a house\n"
line6 = "I do not like them with  a mouse\n"
seussStr = line1+line2+line3+line4+line5+line6
#print(seussStr)
bList = seussStr.splitlines()
print(bList)
'''
