# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate how to build a dictionary

twitterRecord = {}
# Build up a twitter record
handle = input("Enter twitter handle :")
twitterRecord['twitterID'] = handle
name = input("Enter name : ")
twitterRecord['name'] = name
tweets = int(input("Enter number of tweets : "))
twitterRecord['tweets'] = tweets
following = int(input("Enter number for following : "))
twitterRecord['following'] = following
followers = int(input("Enter number of followers : "))
twitterRecord['followers'] = followers

print(twitterRecord)

