import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect(host='den1.mysql6.gear.host',  # your host name is often 'localhost'
                     user='hellodb',            
                     passwd='Ww4A_p~eOXAk',  
                     db='hellodb')        

cur = db.cursor()

# to apply SQL
cur.execute('CREATE TABLE hello (id INT, name VARCHAR(255), brand VARCHAR(255)); ')

for row in cur.fetchall():
    print(row)

db.close()
