# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: To find (and fix) two syntax errors

# A program to display Green Eggs and Ham (v4)

def showChorus():
    print()
    print("I do not like green eggs and ham.")
    print("I do not like them Sam-I-am.")
    print()

def showVerse1():
    print("I do not like them here or there.")
    print("I do not like them anywhere.")
    print("I do not like them in a house")
    print("I do not like them with  a mouse")

def displayVerse2():
    print("I do not like them in a box")
    print("I do not like them with a fox")
    print("I will not eat them in the rain.")
    print("I will not eat them on a train")
    
# Program execution starts here
showChorus()    
displayVerse1() # SYNTAX ERROR 1 - function 'displayVerse1' does not exist
showChorus()
showVerse2() # SYNTAX ERROR 2 - function 'showVerse2' does not exist
showChorus()
