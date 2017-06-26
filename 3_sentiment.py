# -*- coding: utf-8 -*-
import datetime
import unicodedata
import re
from os import path
import matplotlib.pyplot as plt
from googletrans import Translator
from textblob import TextBlob
import csv

def main():
	# Read the whole text.
	text = open('tweetsv2.txt').read()
	text=text.split('\n')
	tweets=[aux.split("|") for aux in text ]
	tweets=[aux for aux in tweets if len(aux)==4 ]
	print len(tweets)
	print tweets[0:4]
	dates={}
	dates['Pinera']=[x[1].replace("+0000 ","") for x in tweets if '@sebastianpinera' in x[2]]
	dates['Guillier']=[x[1].replace("+0000 ","") for x in tweets if '@guillier' in x[2]]
	dates['Goic']=[x[1].replace("+0000 ","") for x in tweets if '@carolinagoic' in x[2]]
	dates['Sanchez']=[x[1].replace("+0000 ","") for x in tweets if '@BeaSanchezYTu' in x[2] or '@labeasanchez' in x[2]]
	dates['Ossandon']=[x[1].replace("+0000 ","") for x in tweets if '@mjossandon' in x[2]]
	dates['Mayol']=[x[1].replace("+0000 ","") for x in tweets if '@AlbertoMayol' in x[2] or '@MayolPresidente' in x[2]]
	dates['Kast']=[x[1].replace("+0000 ","") for x in tweets if '@felipekast' in x[2] ]

	tweet={}
	tweet['Pinera']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@sebastianpinera' in x[2]]
	tweet['Guillier']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@guillier' in x[2]]
	tweet['Goic']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@carolinagoic' in x[2]]
	tweet['Sanchez']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@BeaSanchezYTu' in x[2] or '@labeasanchez' in x[2]]
	tweet['Ossandon']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@mjossandon' in x[2]]
	tweet['Mayol']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@AlbertoMayol' in x[2] or '@MayolPresidente' in x[2]]
	tweet['Kast']=[unicodedata.normalize('NFKD', unicode(x[2],'utf-8')).encode('ASCII', 'ignore') for x in tweets if '@felipekast' in x[2] ]

	#dates=[datetime.datetime.strptime(x,'%a %b %d %H:%M:%S %Y') for x in dates]
	candidatos=['Pinera','Guillier','Goic','Sanchez','Ossandon','Mayol','Kast']
	# Sacar # y @usuarios y traducir y analizar
	sentiment={}
	english={}
	for c in candidatos:
		tweet[c]=[re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",aux).replace(' RT ',' ') for aux in tweet[c]]
		english[c]=list(map(translate,tweet[c]))
		sentiment[c]=list(map(sentimentAnalysis,english[c]))

	with open('Analysis.csv', 'wb') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(['date','spanish','english','sentiment','candidate'])
			for c in candidatos:
				for x in range(0,len(tweet[c])):
					row=[]
					row.append(dates[c][x].encode('latin-1'))
					row.append(tweet[c][x].encode('latin-1'))
					row.append(english[c][x].encode('latin-1'))
					row.append(sentiment[c][x])
					row.append(c.encode('latin-1'))
					wr.writerow(row)



def sentimentAnalysis(iterator):
	if iterator!="":
		analysis = TextBlob(iterator)
		score=analysis.sentiment.polarity
	else:
		score=""
	return score

def translate(iterator):
	translator=Translator()
	try:
		eng=translator.translate(iterator).text
	except:
		eng=""
	return eng

if __name__ == '__main__':
    main()
