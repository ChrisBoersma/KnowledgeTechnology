import wiktionary_reader
#import mysql
#import db
import specifications
import re

#mysql.init()
#mysql.executeCommand("DROP TABLE phones")
specifications.readSpecificationDictionary()
phones = wiktionary_reader.findIPA()
p = phones[0]
specifications = wiktionary_reader.getSpecification(p)
#db.createTable(specifications)
for p in phones:
	specifications = wiktionary_reader.getSpecification(p)
	#print(specifications)
	name = specifications["name"].split(" ", 1)[0]
	print("https://www.kimovil.com/en/where-to-buy-" + name.lower() + "-" + specifications["Soort apparaat"].replace(" ", "-").lower())
	#db.addPhone(specifications)
