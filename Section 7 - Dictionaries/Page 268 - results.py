# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to iterate over dictionaries

#A dictionary to store results for multiple students
results = dict({
    'Joe': 67,
    'Mary' : 76,
    'Alex' : 72,
    'Sarah' : 82,
    'Fred': 64,
    'Pat' : 91,
})

for k in results:
    print(k)

for k in results.keys():
    print(k)

for v in results.values():
    print(v)
   
