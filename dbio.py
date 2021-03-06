import extraction
import filter

def extractInformation():
	db = []
	urls = extraction.getMediaMarktURLs()
	for u in urls:
		specs = extraction.getMediaMarktSpecifications(u)
		kurl = extraction.getKimovilURL(specs)
		if kurl != "":
			specs += extraction.addKimovilSpecifications(kurl)
			specs = dict(specs)
			specs["mediamarkt url"] = u
			specs["kimovil url"] = kurl
			db.append(specs)
	return db

def openDB(filename):
	db = []
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	if len(lines) == 0:
		return db
	keys = lines[0].rstrip().split("\t")
	for i in range(1, len(lines)):
		specs = {}
		values = lines[i].rstrip().split("\t")
		for j in range(min(len(keys), len(values))):
			specs[keys[j]] = values[j]
		db.append(specs)
	return db

def saveDB(filename, db):
	f = open(filename, "w")
	if len(db) == 0:
		return
	i = 0
	keys = []
	for k in db[0]:
		if i > 0:
			f.write("\t")
		else:
			i = 1
		f.write(k)
		keys.append(k)

	for i in range(len(db)):
		f.write("\n")
		for j in range(min(len(keys), len(db[i]))):
			if j > 0:
				f.write("\t")
			if keys[j] in db[i]:
				f.write(db[i][keys[j]].replace("\n", " ").replace("\t", " "))
	f.close()
