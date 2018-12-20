import sys
import requests
import re
import specifications

def findIPA():
	url = 'https://www.mediamarkt.nl/nl/category/_smartphones-483222.html'
	string = requests.get(url).text
	i=0
	page=1
	phones =[]
	while i<20: 
		m2 = re.search('(.*?)/nl/product/(.*?)"(.*)', string, flags = re.DOTALL)
		#print(m2.groups())
		if m2 == None:
			page=page+1
			url = 'https://www.mediamarkt.nl/nl/category/_smartphones-483222.html?page='+str(page)
			string = requests.get(url).text
		else:
			print(str(i) + ": " + str(m2.group(2)))
			phones.append("https://www.mediamarkt.nl/nl/product/"+m2.group(2))
			string = m2.group(3)
			i=i+1
	return phones


def getSpecification(url):
	string = requests.get(url).text
	i=0
	page=1
	phones =[]
	#print(string)
	dic={}
	m2 = re.search('(.*?)"og:title" content="(.*?)"(.*)', string, flags = re.DOTALL)
	dic["name"] = m2.group(2)
	string = m2.group(3)
	#print(string)
	m2 = re.search('(.*?)"product:price:amount" content="(.*?)"(.*)', string, flags = re.DOTALL)
	dic["price"] = m2.group(2)
	string = m2.group(3)
	m = re.split('Productspecificaties', string)
	#print(m)
	string = m[1]
	m = re.split('Toon alle specificaties', string)
	string = m[0]
	numberOfSpecifications = string.count("<dt>")
	#dic["Besturingssysteem"] = "Android 8.0"
	#print("STRRIJNHING: ", string)
	
	while i<numberOfSpecifications: 
		m=re.split('<dt>',string, maxsplit = 1)
		#print("Size of m:" + str(len(m)))
		string=m[1]
		m=re.split(':</dt>',string, maxsplit = 1)
		spec_t = m[0]
		#print("check:", string)
		m=re.split('<dd>', m[1], maxsplit = 1)
		string2=m[1]
		m=re.split('</dd>',string2, maxsplit = 1)
		spec_v =m[0]
		#print("~~~~~:", spec_t, "!!!!!!", spec_v)
		dic[spec_t]=spec_v
		string=m[1]
		#print("Group1:", m.group(1), "\n\nGroup2", m.group(2))
		#dic[m.group(1)]=m.group(3)

	
		i=i+1
	specs = {}
	for k, v in dic.items():
		print(k)
		if k in specifications.dic:
			specs[specifications.dic[k]] = v
	return specs

#words = ["which", "who", "spoonerism", "wiktionary", "football", "world", "photos", "iPhone", "London", "Manchester", "that", "threat", "goal", "keeper", "Chelsea", "FIFA", "Czechoslovakia", "Paris", "United", "column"]

#for word in words:
#	try:
#		print(word, ": ", findIPA(word))
#	except Exception:
#		pass
#phones = findIPA()
#for p in phones:
#	print(getSpecification(p))
#print(findIPA())

