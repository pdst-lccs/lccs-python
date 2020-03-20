# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: To demonstrate syntax errors relating to lists
# To extend thinking in relation to list slicing range errors

suits = ['Hearts','Diamonds','Spades','Clubs']
cardFaces = ['Ace','1','2','3','4','5','6','7','8','9','Jack','Queen','King']

print(cardFaces[1:10])

colourCards = cardFaces[10:23] # This is NOT a syntax error
print(colourCards)

redSuits = suits[:2]
blackSuits = [2:] # Syntax Error 1

print(pinStripSuits) # Syntax Error 2
print(redSuits)
print(blackSuits)



'''
# Bonus (additional) code!
# A program to generate a random card e.g. Ace of Spades
import random

suits=['Hearts','Diamonds','Spades','Clubs']
faces=['A','1','2','3','4','5','6','7','8','9','J','Q','K',]

# 4 suits so ....
# generate a random number between 0 and 3 (inclusive)
r1 = random.randint(0,3)
suit = suits[r1]

# 13 cards so ....
# generate a random number between 0 and 12 (inclusive)
r2 = random.randint(0,12)
face = faces[r2]

card = face+' of '+suit
print(card)
'''
