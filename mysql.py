import pymysql

def executeCommand(command):
	global cur
	cur.execute(command)
	
def getResults():
	global cur
	return cur.fetchall()

def closeDB():
	global db
	db.close()

def init():
	global db
	global cur
	pymysql.install_as_MySQLdb()
	db = pymysql.connect(host='den1.mysql6.gear.host',  # your host name is often 'localhost'
		             user='hellodb',            
		             passwd='Ww4A_p~eOXAk',  
		             db='hellodb')
	cur = db.cursor()
