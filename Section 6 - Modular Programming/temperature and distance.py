# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate some conversion functions

# Convert centigrade to fharenheit
def cent2fhar(centigrade):
    return 9/5*centigrade + 32

# Convert kilometers to miles
def kms2miles(kilometers):
    return( kilometers * 0.62)


# Test cent2fhar
cent = int(input("Enter a value in centigrade: "))
fhar = cent2fhar(cent)
print(cent, "degrees C is", fhar, "degrees F")

# Test kilometers to miles conversion
kms = int(input("Enter a value in kilometers: "))
print("%dkms = %.2fmiles" %(kms, kms2miles(kms)))
