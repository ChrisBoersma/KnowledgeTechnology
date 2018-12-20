import wiktionary_reader
import mysql
import db
import specifications

mysql.init()
#mysql.executeCommand("DROP TABLE phones")
specifications.readSpecificationDictionary()
phones = wiktionary_reader.findIPA()
p = phones[0]
specifications = wiktionary_reader.getSpecification(p)
db.createTable(specifications)
for p in phones:
	specifications = wiktionary_reader.getSpecification(p)
	db.addPhone(specifications)
