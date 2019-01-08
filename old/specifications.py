import re

dic = {}

def readSpecificationDictionary():
	global dic
	F = open("specifications", "r");
	specifications = {}
	for l in F.readlines():
		l = l.rstrip()
		m = re.split("\t", l)
		print(m)
		specifications[m[0]] = m[1]
	F.close()
	dic = specifications
