# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to build a dictionary

# Version 1. A dictionary to store a student's result
results = {}

name = input("Enter student name: ")
results['name'] = name
subject = input ("Enter subject name: ")
mark = input ("Enter percentage mark for "+subject+": ")
results[subject] = mark
print(results)

