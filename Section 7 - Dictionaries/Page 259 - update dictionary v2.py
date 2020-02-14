# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to update a dictionary

d1 = {
    "OMG" : "Oh My God!",
    "LOL" : "Laugh out Loud",
    "IMHO" : "In My Humble Opinion",
}

d2 = {
     "LOL" : "League of Legends",
}

print(d1)
d1.update(IMHO = "In My Honest Opinion")
d1.update(d2)
print(d1)

