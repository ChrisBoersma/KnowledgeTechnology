usedSpecs = {}

def filter(specs):
	filteredSpecs = {}
	for k in specs:
		if k in usedSpecs:
			filteredSpecs[usedSpecs[k]] = specs[k]
	return filteredSpecs

def filterDB(db):
	db2 = []
	for d in db:
		db2.append(filter(d))
	return db2

def readUsedSpecs():
	global usedSpecs
	F = open("specifications", "r");
	usedSpecs = {}
	for l in F.readlines():
		l = l.rstrip()
		m = l.split("\t")
		usedSpecs[m[0]] = m[1]
	F.close()

def init():
	readUsedSpecs()

init()
