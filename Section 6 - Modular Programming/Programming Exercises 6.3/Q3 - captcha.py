# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q3
# Purpose: A program to generate and validate a CAPTCHA

import random

def generateNewCAPTCHA():

    global captcha
    # generate a random number between 65 (A) and 90 (Z)
    for i in range(4):
        randomNo = random.randint(65, 90)
        #print(randomNo)
        #print(chr(randomNo))
        captcha = captcha + chr(randomNo)
   

def displayCAPTCHA():
    print("Prove that you are not a computer")
    print("The CAPTCHA is shown here >>>", captcha)
    

def isValid():
    userEntry = input("Enter the CAPTCHA here >>> ")
    return userEntry == captcha


captcha = ""
generateNewCAPTCHA()
displayCAPTCHA()
if isValid():
    print("Correct!")
else:
    print("Incorrect!")
