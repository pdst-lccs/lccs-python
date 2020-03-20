# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to create survey.html by inserting data
# read from survey.txt into a survey template file

# Open the survey template
htmlFile = open("survey_template.html","r", encoding="utf-8") # Open the file
htmlStr = htmlFile.read()
htmlFile.close() # close the file

# Open the data file
surveyFile = open("survey.txt","r")
surveyQuestion = surveyFile.readline()

#---------------------------------------#
#       *** YOUR CODE GOES HERE ***     #
#---------------------------------------#

surveyFile.close() # close the file

# Now replace the 'markers' from the template file with the runtime data
htmlStr2 = htmlStr.replace("<QUESTION>", surveyQuestion)

#---------------------------------------#
#       *** YOUR CODE GOES HERE ***     #
#---------------------------------------#


# Write the survey page
htmlFile = open("survey.html","w", encoding="utf-8") # Open the file for writing
htmlFile.write(htmlStr2)
htmlFile.close() # close the file


