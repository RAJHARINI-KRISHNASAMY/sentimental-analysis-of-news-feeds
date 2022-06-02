import feedparser
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
d = feedparser.parse('http://feeds.foxnews.com/foxnews/politics')
d1=feedparser.parse('http://feeds.foxnews.com/foxnews/national')
d2=feedparser.parse('http://feeds.foxnews.com/foxnews/world')
d3=feedparser.parse('http://feeds.foxnews.com/foxnews/latest')
heading=['field','title','summary','cleaned_summary']
title=[]
summary=[]
field=[]
for post in d.entries:
    field.append('politics')
    title.append(post['title'])
    summary.append(post['summary'])
for post in d1.entries:
    field.append('national')
    title.append(post['title'])
    summary.append(post['summary'])
for post in d2.entries:
    field.append('world')
    title.append(post['title'])
    summary.append(post['summary'])
for post in d3.entries:
    field.append('latest')
    title.append(post['title'])
    summary.append(post['summary'])
s1=[]
stop_words_rm=[]
for s in summary:
    s= re.sub('<.*?>',"",s)
    s= re.sub('\xa0',"",s)
    s=s.replace('\\', ' ')
    s=s.lower()
    s1.append(s)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(s)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words] 
    filtered_sentence = (" ").join(filtered_sentence)
    stop_words_rm.append(filtered_sentence)
df = pd.DataFrame(list(zip(field,title, s1,stop_words_rm)),
               columns =heading)
print(df)