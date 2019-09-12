#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Angela McNeese
# Word Frequency Counter
# Data Science for Innovators
# Date:


# In[2]:


# Write a program that downloads a web page requested by the user and 
# reports up to ten most frequently used words. The program should treat 
# all words as case-insensitive. For the purpose of this exercise, 
# assume that a word is described by the regular expression r"\w+". 


# In[3]:


# Imports
import urllib.request
import urllib.parse
import pandas
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter


# In[ ]:


# Get a request from the user for a web page
url = input("Enter a URL: ")
try:
    doc = urllib.request.urlopen(url)
except:
    print("Could not open %s" % url)


# In[ ]:


# html = doc.read().decode().lower()
# print(html)


# In[ ]:


# Download the requested web page
try:
    html = doc.read()
except:
    print("Could not read. My bad.")
print(html)


# In[ ]:


try:
    decoded = html.decode()
except:
    print("Could not decode. Sorry!")
print(decoded)


# In[ ]:


#  - treat all words as case insensitive : lower()
try:
    lowered = decoded.lower()
except:
    print("Could not translate. Sorry!")
print(lowered)


# In[ ]:


# reports up to 10 of the most frequently used words
count = re.findall(r"\w+", lowered)


# In[ ]:


# Count the words and report
print(Counter(count).most_common(10))


# In[ ]:





# In[ ]:


# "File Indexer"


# In[ ]:


# Write a program that indexes all files in a certain user-designated directory (folder). 
# The program should construct a dictionary where the keys are all unique words in all the files 
# (as described by the regular expression r"\w+"; treat the words as case-insensitive), 
# and the value of each entry is a list of file names that contain the word. For instance, if the word “aloha”
# is mentioned in the files “early-internet.dat” and “hawaiian-travel.txt,” the dictionary will have an entry 
# {...,'aloha':['early-internet.dat','hawaiian-travel.txt'],...}. 
# The program will pickle the dictionary for future use. 


# In[ ]:


# Imports


# In[ ]:


# User Designates a directory(folder)


# In[ ]:


# read files

with open(name, mode="r") as f:


# In[ ]:


# Construct a dictionary where the keys are all unique words in all the files as described by r"\w+" case-insensitive
files = #Input 
cntr = Counter(words.split()) cntr.most_common(


# In[ ]:


# Pickle the dictionary for later use
pickledDict = dict(cntr.most_common())


# In[ ]:


with open(myFile.csv, newline='') as infile:
    reader = csv.reader(infile, delimiter=',', quotechar='"')


# In[1]:


with open("myFile.csv", newline='') as infile:
    data = list(csv.reader(infile))


# In[2]:


"52" + 52


# In[3]:


int('52') + 52


# In[ ]:




