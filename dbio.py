import extraction
import filter

def extractInformation():
	db = []
	urls = extraction.getMediaMarktURLs()[:2]
	#urls = ["https://www.mediamarkt.nl/nl/product/_wiko-sunny3-mini-8gb-dual-sim-zwart-1601156.html", "https://www.mediamarkt.nl/nl/product/_nokia-1-2018-8gb-dual-sim-rood-1562780.html"]
	for u in urls:
		specs = extraction.getMediaMarktSpecifications(u)
		#print("Loop: " + u)
		kurl = extraction.getKimovilURL(specs)
		if kurl != "":
			specs += extraction.addKimovilSpecifications(kurl)
			specs = dict(specs)
			print(specs)
			#print(kurl)
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


db = openDB("dbsavefile2")
#db = filter.filterDB(db)
#saveDB("dbsavefile1", db)\
db2 = []
i=0
for specs in db:
	kurl = extraction.getKimovilURL(specs)
	if kurl != "":
		specs2 = extraction.addKimovilSpecifications(kurl)
		
		#print("~~~~~~~~~~~~~~~~~~~~")
		#for i in specs2:
		for (v, k) in specs2:
			specs[v] = k
		#	specs = dict(specs)
		#print(specs)
		#specs = dict(specs)
		#print(specs)		
		#print(kurl)
		#specs["mediamarkt url"] = u
		specs["kimovil url"] = kurl
		if "Is it comfortable?" in specs:
			db2.append(specs)
	
#print(db2[0])
db2 = filter.filterDB(db2)
saveDB("dbsavefile0", db2)



#extractInformation()