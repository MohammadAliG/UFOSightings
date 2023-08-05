import requests
from bs4 import BeautifulSoup
import time

class UFO:
	def __init__(self, cities, num):
		self.cities = cities
		self.num = num

	def print(self):
		print(self.cities.print() + "\t" + str(self.num))
class Cities:
	def __init__(self, city, state):
		self.city = city
		self.state = state
		
	def print(self):
		print(self.city + "," + self.state)

url = "http://www.cs.umd.edu/~golbeck/INST326/ndxLocOut.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.findAll("a")
#print(links)

i = 1
while i < len(links):
	url = links[i]["href"]
	#print(url)
	data = requests.get(url)
	soup2 = BeautifulSoup(data.content, "html.parser")
	tb = soup2.find('tbody')
	info = tb.find_all('td')
	print(info.get_text())

	#soup2 = BeautifulSoup(data.text, "html.parser")
	#info = soup2.findAll("tr")
	#print(info)
	#j = 1
	#while j < len(info):
	#	lines = info[j].split("td>")
	#	print(lines[1])
	#	j += 1

	time.sleep(5)
	i += 1