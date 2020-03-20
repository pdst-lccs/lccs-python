# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to read and display a web page


# A program to read and display a web page
import urllib.request

# Open the URL
page = urllib.request.urlopen("https://www.compsci.ie/")
# Read and decode
text = page.read().decode("utf8")
# Display
print(text)

'''
# IDEA:
# The above code could be used as a basis for further development by students
'''
