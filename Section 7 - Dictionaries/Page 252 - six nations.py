# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate dictionary indexing


capitals = {
    "Ireland" : "Dublin",
    "Scotland" : "Edinburgh",
    "England" : "London",             
    "Wales" : "Cardiff",
    "France" : "Paris",
    "Italy" : "Rome"
}

country = input("Enter one of the six nations : ")
print("The capital of "+country+" is "+capitals[country])
