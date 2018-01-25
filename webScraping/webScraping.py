#!usr/bin/python

import requests
from bs4 import BeautifulSoup
#import bs4

r = requests.get("http://pythonhow.com/example.html")

value = r.content


soup = BeautifulSoup(value, "html.parser")

#print (soup.prettify())

alldata=soup.find_all("div",{"class":"cities"})

print (alldata[0].find_all("h2")[0].text)

for i in alldata:
	print (i.find_all("p")[0].text)
