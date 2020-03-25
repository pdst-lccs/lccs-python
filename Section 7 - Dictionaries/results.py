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

# Display the keys
print("Display the keys")
for key in results.keys():
    print("Name: %s" %key)
print("-----------")

# A simpler way to display the keys
print("A simpler way to display the keys")
for key in results:
    print("Name: %s" %key)
print("-----------")

# Display the keys - sorted
print("Display the keys - sorted")
for key in sorted(results):
    print("Name: %s" %key)
print("-----------")

# Display the values
print("Display the values")
for value in results.values():
    print("Value: %s" %value)
print("-----------")   
