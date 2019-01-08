import mysql

tableName = "phones"

def createTable(specifications):
	q = "CREATE TABLE " + tableName + " ("
	i = 0
	for s in specifications:
		if i == 1:
			q += ', '
		else:
			i = 1
		q += s+ " VARCHAR(255)"
	q += ");"
	print(q)
	mysql.executeCommand(q)

def addPhone(specifications):
	global tableName
	q = "INSERT INTO " + tableName + " ("
	columns = ""
	values = ""
	i = 0
	for key, value in specifications.items():
		if i == 1:
			columns += ', '
			values += ', '
		else:
			i = 1
		columns += key
		values += "'" + value + "'"
	q += columns + ") VALUES (" + values + ");"
	print("")
	print(q)
	print("")
	mysql.executeCommand(q)
