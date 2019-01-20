import re
import requests

def getMediaMarktURLs():
	url = 'https://www.mediamarkt.nl/nl/category/_smartphones-483222.html'
	phones = []
	for i in range(1, 5):
		string = requests.get(url + "?page=" + str(i)).text
		newURLs = re.findall('(/nl/product/.*?.html)"', string)
		for n in newURLs:
			phones.append("https://www.mediamarkt.nl" + n)
	return list(set(phones))

def getMediaMarktSpecifications(url):
	string = requests.get(url).text
	specifications = re.findall('"(.*?)" content="(.*?)"', string)
	r = re.search("Productspecificaties(.*?)Toon alle specificaties", string, flags = re.DOTALL)
	if r == None:
		raise ValueError
	string = r.group(1)
	specifications += re.findall("<dt>(.*?):</dt>.*?<dd>(.*?)</dd>", string, flags = re.DOTALL)
	return specifications

def getKimovilURL(specs):
	specs = dict(specs)
	names = ["" for i in range(5)]
	name = specs["og:title"]
	brand = name.split(" ")[0]
	names[0] = brand + "-" + specs["Soort apparaat"]
	m = re.split(" 20\d+", name1)
	names[1] = m[0]
	m = re.split(" \d+ *GB", name)
	names[2] = m[0]
	r = re.search("(\S)(\d)", name1)
	names[3] = re.sub(r"(\S)(\d)", r"\1 \2", name1)
	if names[0] == "HONOR-Honor 8X":
		names[4] = "huawei-8x"
	i = 0
	start = True
	string = ""
	while i in range(len(names)) and (start or "Error 404" in string):
		url = "https://www.kimovil.com/en/where-to-buy-" + names[i].replace(" ", "-").replace(".", "-").lower()
		string = requests.get(url).text

	if "Error 404" in string:
		return ""
	return url

def addKimovilSpecifications(url):
	string = requests.get(url).text
	results = re.findall('<dt>(.*?)</dt>\n<dd class="average">\n<ul class="user-val-overall-dist mini">\n<li><div class="g-bar dist-bar9" style="width: (.*?)%;"></div>', string)
	results = list(results)
	r = re.search('"partials": (.*?)}}', string)
	s = r.group(1) + ","
	results += re.findall('"(.*?)": (.*?),', s)
	return results
