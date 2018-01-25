#!usr/bin/python
import pandas
import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

content = r.content

#HTML Source
soup = BeautifulSoup(content,"html.parser")


allData = soup.find_all("div", {"class":"property-card-primary-info"})

allData[0].find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")


l=[]
#goes through all the houses
for item in allData:
	dictionary = {}
	dictionary["Price"] = item.find("a", {"class":"listing-price"}).text.replace("\n","").replace(" ","")
	dictionary["PropertyAddress"] = item.find("div", {"class":"property-address"}).text.replace("\n","").replace(" ","")
	dictionary["City"] =  item.find("div", {"class":"property-city"}).text.replace("\n","").replace(" ","")

	try:
		dictionary["Bedrooms"] =  item.find("div", {"class":"property-beds"}).text.replace("\n","").replace(" ","")
	except:
		dictionary["Bedrooms"] = None
	try:
		dictionary["Bathrooms"] = item.find("div", {"class":"property-baths"}).text.replace("\n","").replace(" ","")
	except:
		dictionary["Bathrooms"] = None

	try:
		dictionary["PropertySize"] = item.find("div", {"class":"property-sqft"}).text.replace("\n","").replace(" ","")
	except:
		dictionary["PropertySize"] = None

	l.append(dictionary)
#print (l)

df = pandas.DataFrame(l)

df.to_csv("/Users/Roy/Desktop/Output.csv")


