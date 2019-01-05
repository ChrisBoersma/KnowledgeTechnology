usedSpecs = {}

def filter(specs):
	filteredSpecs = {}
	for k, v in specs:
		if k in usedSpecs:
			filteredSpecs[usedSpecs[k]] = v
	return filteredSpecs

def readUsedSpecs():
	global usedSpecs
	F = open("specifications", "r");
	usedSpecs = {}
	for l in F.readlines():
		l = l.rstrip()
		m = l.split("\t")
		print(m)
		usedSpecs[m[0]] = m[1]
	F.close()

def init():
	readUsedSpecs()

init()
