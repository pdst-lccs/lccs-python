# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of dictionaries to calculate the mean result

#A dictionary to store results for multiple students
results = {
    'Joe': 67,
    'Mary' : 76,
    'Alex' : 72,
    'Sarah' : 82,
    'Fred': 64,
    'Pat' : 91,
}

# Calculate the mean v1
total = 0
for v in results.values():
    total = total + v

mean_result = total/len(results)
print("Mean result: %d " %mean_result)

