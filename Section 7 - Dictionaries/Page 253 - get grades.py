# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate dictionary 'get' method

grades = {
    "Irish" : "H3",
    "English" : "O3",
    "Maths" : "H4",             
    "Computer Science" : "H1",
}

subject = input ("Enter subject name: ")
result = grades.get(subject)
print("Result for %s was %s" %(subject, result))
print(grades)
