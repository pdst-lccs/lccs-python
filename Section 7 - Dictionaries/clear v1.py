# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to clear a dictionary

d1 = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

d2 = {
     "LOL" : "League of Legends",
}

d1.clear()
del d2['LOL']

print(d1)
print(d2)
