# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Partial solution to breakout 4.1 - random sentence generator
# The full solution needs to be developed further ....

import random

# Initialise the lists of words
article = ['the', 'a', 'one', 'some', 'any']
noun    = ['teacher', 'student', 'principal', 'library', 'school']
verb    =   ['taught', 'learned', 'read', 'walked', 'ran']
preposition =['to', 'from', 'over', 'under', 'on']

# Set the sentence wordList to be initially blank
wordList = []

# Choose a random article by using a random number as an index
r = random.randint(0,4)
word = article[r]
wordList.append(word)

# Choose a random noun by using the choice command (method)
word = random.choice(noun)
wordList.append(word)

# Display the sentence (so far)
print(wordList[0]+" "+wordList[1])


# Keep going! Get the next word ...
