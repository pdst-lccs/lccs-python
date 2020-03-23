import re
from collections import Counter
import plotly.plotly
from plotly.graph_objs import Bar, Layout


word = []
word_count = []

file = open("sample_text.txt","r") #http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

string = file.read()

file.close()

clean_string = re.sub('[^a-zA-Z0-9 \n\.]', ' ', string) #https://lzone.de/blog/Python+re.sub+Examples
clean_string = re.sub('[0-9]', ' ', clean_string)
clean_string = re.sub('\t', ' ', clean_string)
clean_string = re.sub('\n', ' ', clean_string)
clean_string = re.sub(r'\b\w{1,4}\b', '', clean_string) # removes words three or less charcters https://stackoverflow.com/questions/24332025/remove-words-of-length-less-than-4-from-string
clean_string = re.sub('   ', ' ', clean_string)
clean_string = re.sub('  ', ' ', clean_string)
clean_string = re.sub('\.', '', clean_string)
clean_string = re.sub('â€™', '', clean_string)
clean_string = re.sub('â€“', '', clean_string)
clean_string = clean_string.lower()

string_array = clean_string.split(' ')
string_array = [x for x in string_array if x != ''] #https://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value

c = Counter(string_array)       #https://pymotw.com/2/collections/counter.html

unique_elements = set(string_array) #https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

for letter in unique_elements:
    word.append(letter)         #https://www.thegeekstuff.com/2013/06/python-list/?utm_source=feedly
    word_count.append(c[letter])

print ('Most common:')
for letter, count in c.most_common(20):
    print('%s: %7d' % (letter, count))

plotly.offline.plot({           #https://plot.ly/python/getting-started/#initialization-for-offline-plotting
    "data": [Bar(x=word, y=word_count)],
    "layout": Layout(title="word count")
})



# If possible collect samples from your peers and compare the vocabulary distribution, avergae number of words, word frequency etc.
#
