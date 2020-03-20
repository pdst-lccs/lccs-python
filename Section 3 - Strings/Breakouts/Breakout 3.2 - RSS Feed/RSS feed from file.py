# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: To read and display a live RSS feed using
# a URL read from a text file (feeds.txt)

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



# START HERE ... (ignore all lines before this point)

# Page 92 Q2 - Hint #2
feedFile = open("feeds.txt", "r")
feedURL = feedFile.readline()
feedFile.close()
feed = getRSSString(feedURL)

# Display the feed
print(feed)

# Display the number of lines
print("There are %d lines in this feed\n" %feed.count("\n"))

# Page 92 - Q4
# Make it look like the news is coming from IBM .....
fakeNews = feed.replace("RTÉ", "IBM")
print(fakeNews) # Save to a file? HTML?

# Page 93 - Q6
words = feed.split()
print(collections.Counter(words).most_common(5))

