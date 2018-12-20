import pymysql

def executeCommand(command):
	global cur
	global res
	global db
	res = cur.execute(command)
	print(res)
	db.commit()
	
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
"INSERT INTO phones (Screen_diagonal, Camera_resolution, Operating_System, Frontcamera_resolution, Maximum_sd_card_capacity) VALUES ('6.0 inch', '24 + 5 + 8 megapixel', 'Android 8.0', '24 megapixel', '256 GB');"

