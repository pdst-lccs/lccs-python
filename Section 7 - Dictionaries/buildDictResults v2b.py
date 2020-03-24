# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to build a dictionary

# Version 2b. A dictionary to store multiple results for a student
results = {}

name = input("Enter student name: ")
results['name'] = name
subject = input ("Enter subject name: ")
while subject != "":
    mark = input ("Enter percentage mark for "+subject+": ")
    results[subject] = mark
    subject = input ("Enter subject name: ")

print(results)

