import re
import requests

def getMediaMarktURLs():
	url = 'https://www.mediamarkt.nl/nl/category/_smartphones-483222.html'
	phones = []
	for i in range(1, 2):
		string = requests.get(url + "?page=" + str(i)).text
		newURLs = re.findall('(/nl/product/.*?)"', string)
		for n in newURLs:
			phones.append("https://www.mediamarkt.nl" + n)
	return [list(set(phones))[0]]

def getMediaMarktSpecifications(url):
	string = requests.get(url).text
	specifications = re.findall('"(.*?)" content="(.*?)"', string)
	r = re.search("Productspecificaties(.*?)Toon alle specificaties", string, flags = re.DOTALL)
	if r == None:
		raise ValueError
	string = r.group(1)
	specifications += re.findall("<dt>(.*?):</dt>.*?<dd>(.*?)</dd>", string, flags = re.DOTALL)
	specifications = dict(specifications)
	#print(specifications)
	return specifications

def addKimovilURL(specs):
	pass

def addKimovilSpecifications(specs):
	pass

#urls = getMediaMarktURLs()
#for u in urls:
#	getMediaMarktSpecifications(u)
