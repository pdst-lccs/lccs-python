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

##ask user to add another article
newArticle = input("Add another article, e.g. 'an': ")
article.append(newArticle)

##ask user to add another noun
newNoun = input("Add another noun, e.g. 'special needs assistant' or 'office': ")
article.append(newNoun)

##ask user to add another verb
newVerb = input("Add another verb, e.g. 'understood': ")
article.append(newVerb)

##ask user to add another preposition
newPreposition = input("Add another preposition, e.g. 'for': ")
article.append(newPreposition)


# Set the sentence wordList to be initially blank
wordList = []

# Choose a random article by using a random number as an index
r = random.randint(0,4)
word = article[r]
wordList.append(word.capitalize())

# Choose a random noun by using the choice command (method): alternative implementation
word = random.choice(noun)
wordList.append(word.capitalize())

#3rd word
word = random.choice(verb)
wordList.append(word)
#4th word
word = random.choice(article)
wordList.append(word)
#5th word
word = random.choice(noun)
wordList.append(word.capitalize())
#6th word
word = random.choice(preposition)
wordList.append(word)
#7th word
word = random.choice(verb)
wordList.append(word)

print(wordList)

#Extension exercise #1 - capitalise the first word and any nouns in the sentence
#Extension exercise #2 - ask the user to enter more articles, more nouns, more verbs,more prepositions & add to the appropriate list
#Extension exercise #3 - create a second sentence
#Extension exercise #4 - make the nouns plural