#!usr/bin/python3
import re
import pandas
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
# https://www.bac-lac.gc.ca/eng/census/1901/Pages/item.aspx?itemid=3691959
idNum = 30


l=[]
baseURL = ("https://www.bac-lac.gc.ca/eng/census/1901/Pages/item.aspx?itemid=")
for page in range(1,idNum,1):
	print (baseURL+str(page))
	testNum = str(page)
	r = requests.get("https://www.bac-lac.gc.ca/eng/census/1901/Pages/item.aspx?itemid="+testNum, timeout=None)
	#test = requests.get("https://www.bac-lac.gc.ca/eng/census/1901/Pages/item.aspx?itemid="+testNum).elapsed.total_seconds()
	#print ("Time: ", test)
	#code = (r.status_code)

	#if code != 200:
	#	break

	content = r.content
	soup = BeautifulSoup(content,"html.parser")

	allData = soup.find_all("p")

	dictionary = {}
	for item in allData:
		#print("item: ", item)
		try: 
			
			line = (item.find("strong").text)
			
			if line in "Given Name: ":
				givenName = (item.text)
				titleGivenName, handleGivenName = givenName.split(": ")
				dictionary["GivenName"] = handleGivenName
			
			elif line in "Surname: ":
				surname = (item.text)
				titleSurname, handleSurname = surname.split(" ")
				dictionary["Surname"] = handleSurname

			elif line in "Gender: ":
				gender = (item.text)
				titleGender, handleGender= gender.split(": ")
				dictionary["Gender"] = handleGender

			elif line in "Age: ":
				age = (item.text)
				titleAge, handleAge= age.split(": ")
				dictionary["Age"] = handleAge

			elif line in "Occupation: ":
				occupation = (item.text)
				titleOccupation, handleOccupation= occupation.split(": ")
				dictionary["Occupation"] = handleOccupation

			elif line in "Birth Date: ":
				birthDate = (item.text)
				titleBirthDate, handleBirthDate= birthDate.split(": ")
				dictionary["BirthDate"] = handleBirthDate


		except Exception as e: 
			print(e)

	l.append(dictionary)
df = pandas.DataFrame(l)

