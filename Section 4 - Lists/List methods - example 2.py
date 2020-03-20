# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: NCCA/PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of list specific methods

# Sample program to build up a list
userList = []
userName = input("Enter your name: ")
userList.append(userName)
userAge = int(input("What age are you "+userName+"?"))
userList.append(userAge)
userCountry = input("What is your country of birth?")
userList.append(userCountry)

print("My database for "+userName+"\n"+str(userList))

