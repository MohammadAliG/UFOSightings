import requests
import re

myKey = "3scNXn68VbMZO9uRi6A7J4O4Egi2ogWY"

file = open("Documents/Python/latlon/UFO_data.txt")
fOut = open("Documents/Python/latlon/gholamimehrabadi_mohammadali_latlon.txt", "w")

while True:
	line = file.readline()
	if(len(line) == 0):
		break
	line = re.sub(r" ?\([^)]+\)", "", line)
	line = line.replace("(", "")
	line = line.replace(")", "")
	l = line.split("\t")
	location = l[0]
	count = l[1].replace("\n", "")
	url = 'http://open.mapquestapi.com/geocoding/v1/address?outFormat=csv&key='+myKey+'&location='+location
	results = requests.get(url)
	results = results.text.split(",")
	lat = results[len(results) - 2]
	lon = results[len(results) - 1]
	lat = lat.replace('"', "")
	lon = lon.replace('"', "")
	latlon = lat + ", " + lon
	fOut.write(latlon + "\t" + count + "\n")

file.close()
fOut.close()