# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to sort dictionaries

#A dictionary to store results for multiple students
results = dict({
    'Joe': 67,
    'Mary' : 76,
    'Alex' : 72,
    'Sarah' : 82,
    'Fred': 64,
    'Pat' : 91,
})

# Display the items of the dictionary as Python stores them
for k,v in results.items():
    print("Name: %s Result: %d" %(k,v))


# Display the items of the dictionary in a sorted order
for k,v in sorted(results.items()):
    print("Name: %s Result: %d" %(k,v))

# A more advanced sort - this time by values
import operator
for k, v in sorted(results.items(), key=operator.itemgetter(1)):
    print("Name: %s Result: %d" %(k,v))
