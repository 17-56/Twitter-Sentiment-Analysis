# -*- coding: utf-8 -*-
import unicodedata
import re
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from googletrans import Translator

# Read the whole text.
text = open('tweetsv2.txt').read()
text=text.split('\n')
tweets=[aux.split("|") for aux in text ]
tweets=[aux for aux in tweets if len(aux)==4 ]


tweets=[unicodedata.normalize('NFKD', unicode(aux[2],'utf-8')).encode('ASCII', 'ignore') for aux in tweets]
tweets=list(set(tweets))
print "Number of tweets: %s" % (len(tweets))

# Sacar # y @usuarios
tweets=[re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux) for aux in tweets]

#Translate
translator=Translator()
print translator.translate(tweets[0]).text
