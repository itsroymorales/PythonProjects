#!usr/bin/python
import pandas
import requests
from bs4 import BeautifulSoup


id = "3600000"
r = requests.get("https://www.bac-lac.gc.ca/eng/census/1901/Pages/item.aspx?itemid="+id)
content = r.content
soup = BeautifulSoup(content,"html.parser")

allData = soup.find_all("div", {"class":"col-md-6"})
#content = r.content
allData[0].find("p", {"class":"col-md-6"})
print (allData)
#HTML Source
#soup = BeautifulSoup(content,"html.parser")
