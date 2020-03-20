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
surveyAnswer1  = surveyFile.readline()
surveyAnswer2  = surveyFile.readline()
surveyFile.close() # close the file

# Now replace the 'markers' from the template file with the runtime data
htmlStr2 = htmlStr.replace("<place-holder-1>", surveyQuestion)
htmlStr2 = htmlStr2.replace("<place-holder-2>", surveyAnswer1)
htmlStr2 = htmlStr2.replace("<place-holder-3>", surveyAnswer2)

# Write the survey page
htmlFile = open("survey.html","w", encoding="utf-8") # Open the file for writing
htmlFile.write(htmlStr2)
htmlFile.close() # close the file


