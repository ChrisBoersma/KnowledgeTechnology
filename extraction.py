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
	#specifications = dict(specifications)
	##print(specifications)
	return specifications

def getKimovilURL(specs):
	specs = dict(specs)
	name = specs["og:title"]
	brand = name.split(" ")[0]
	##print(specs)
	name1 = brand + "-" + specs["Soort apparaat"]
	#print("Name1 " + name1)
	m = re.split(" 20\d+", name1)
	name2 = m[0]
	#print("Name2 " + name2)
	m = re.split(" \d+ *GB", name)
	name3 = m[0]
	r = re.search("(\S)(\d)", name1)
	#if r != None:
	#	#print(r.group(1), r.group(2))
	#else:
	#	#print("None")
	name4 = re.sub(r"(\S)(\d)", r"\1 \2", name1)
	name5 = ""
	if name1 == "HONOR-Honor 8X":
		name5 = "huawei-8x"
	#name3 = m[0]
	url = "https://www.kimovil.com/en/where-to-buy-" + name1.replace(" ", "-").replace(".", "-").lower()
	#print("Tried 1: " + url)

	string = requests.get(url).text
	if "Error 404" in string:
		url = "https://www.kimovil.com/en/where-to-buy-" + name2.replace(" ", "-").replace(".", "-").lower()
	#print("Tried 2: " + url)

	string = requests.get(url).text
	if "Error 404" in string:
		m = re.split(" \d+ *GB", specs["og:title"])
		url = "https://www.kimovil.com/en/where-to-buy-" +name3.replace(" ", "-").replace(".", "-").lower()
	#print("Tried 3: " + url)
	
	string = requests.get(url).text
	if "Error 404" in string:
		#m = re.split(" \d+ *GB", specs["og:title"])
		url = "https://www.kimovil.com/en/where-to-buy-" +name4.replace(" ", "-").replace(".", "-").lower()

	string = requests.get(url).text
	if "Error 404" in string and name5 != "":
		#m = re.split(" \d+ *GB", specs["og:title"])
		url = "https://www.kimovil.com/en/where-to-buy-" +name5.replace(" ", "-").replace(".", "-").lower()

	#print("Tried 3: " + url)
	string = requests.get(url).text
	if "Error 404" in string:
		#print("Not yet perfect...")
		#print("Troublesome url: " + url)
		return ""
		#raise ValueError
	return url

def addKimovilSpecifications(url):
	string = requests.get(url).text
	results = re.findall('<dt>(.*?)</dt>\n<dd class="average">\n<ul class="user-val-overall-dist mini">\n<li><div class="g-bar dist-bar9" style="width: (.*?)%;"></div>', string)
	#print("check : ", list(results))
	#print("~~~~~~~~~~~~~~~~~~~~")
	results = list(results)
	r = re.search('"partials": (.*?)}}', string)
	s = r.group(1) + ","
	results += re.findall('"(.*?)": (.*?),', s)
	return results
	##print(list(dict(results)))
	#pass

#urls = getMediaMarktURLs()
#for u in urls:
#	getMediaMarktSpecifications(u)
##print(getKimovilURL({"og:title": "SAMSUNG Galaxy J6 2018 32GB Dual-sim Zwart"}))

#addKimovilSpecifications("https://www.kimovil.com/en/where-to-buy-samsung-galaxy-s8")
