import mysql
mysql.init()
mysql.executeCommand("DESCRIBE phones")
print(mysql.getResults())
mysql.executeCommand("SELECT * FROM phones")
print(mysql.getResults())
print(mysql.res)
for result in mysql.res:
     if result.with_rows:
             print(result.statement)
             print(result.fetchall())
     else:
             print(result.statement)
             print(result.rowcount)

