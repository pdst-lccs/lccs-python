# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: To read and display Apple's live RSS feed

from urllib.request import urlopen
from xml.dom import minidom
import collections

# extract the headlines from the feed
def extractString(doc):
   str = ""
   for node in doc.getElementsByTagName('channel'):
      for title in node.getElementsByTagName('title'):
         str = str + title.firstChild.data + "\n"
   return str

# extract the feed from the url
def getRSSString(url):
    results = []
    rssString = ""
    results.append(minidom.parse(urlopen(url)))
    for webDoc in results:
        rssString = rssString + extractString(webDoc)
    return rssString


# PROGRAM START FROM HERE 
# (ignore all lines before this point)

# Read the RSS feed from the URL provided
feed = getRSSString("https://www.apple.com/main/rss/hotnews/hotnews.rss")
# Display the results
print(feed)
# Display the number of lines
print("There are %d lines in this feed" %feed.count("\n"))
