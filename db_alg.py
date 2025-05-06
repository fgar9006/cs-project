import sqlite3, os, os.path
bdir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(bdir, "pmg.db")

def signup(usn,pasw,rpasw):
	#with sqlite3.connect("pmg.db") as db:
	with sqlite3.connect(db_path) as db:
		c=db.cursor()
	run=True
	while run:
		find_user=("SELECT * FROM user WHERE username=?")
		c.execute(find_user,[(usn)])
		if c.fetchall():
			ret=1 #username is taken
			run=False
		elif pasw!=rpasw:#re-entered password doesn't match
			ret=2
			run=False
		else:
			#inserts details into database
			insertdata=("INSERT INTO user(username,password) VALUES (?,?)")
			c.execute(insertdata,[(usn),(pasw)])
			#retrieve the userID
			getID=("SELECT userID FROM user WHERE username=? and password=?")
			c.execute(getID,[(usn),(pasw)])
			rows=c.fetchall()#returns as a tuple
			#converts tuple to use the userID
			columns=[desc[0] for desc in c.description]
			results=[dict(zip(columns,row)) for row in rows] #converts into a dictionary
			user_ID=[row[0] for row in rows]#accesses the userID
			num=int(user_ID[0])#typecast into an integer
			#set the current score to 0 for the specific userID
			createscore=("INSERT INTO scores(userID,curscore) VALUES(?,?)")
			c.execute(createscore,[(num),(0)])
			db.commit()
			db.close()
			ret=3
			run=False
	return ret,0#returns command and current score


def login(usn,pasw):
	#with sqlite3.connect("pmg.db") as db:
	with sqlite3.connect(db_path) as db:
		c=db.cursor()
	find_user=("SELECT password FROM user WHERE username=?")
	c.execute(find_user,[(usn)])
	rows=c.fetchall()
	if rows==[]:#if there's nothing is results, username unrecognised
		return 1,0
	#converts tuple to use the password
	columns=[desc[0] for desc in c.description]
	results=[dict(zip(columns,row)) for row in rows] #converts into a dictionary
	password=[row[0] for row in rows]#accesses the password in db
	results=password[0]
	if results!=pasw:
		db.close()
		return 2,0#if username found but password is wrong
	else:
		#finds the userID
		find_user='SELECT userID FROM user WHERE username=?'
		c.execute(find_user,[(usn)])
		rows=c.fetchall()
		#converts tuple to use the userID
		columns=[desc[0] for desc in c.description]
		results=[dict(zip(columns,row)) for row in rows] #converts into a dictionary
		userID=[row[0] for row in rows]#accesses the userID in db
		usID=userID[0]

		#retrives the current score using the userID
		get_score='SELECT curscore FROM scores WHERE userID=?'
		c.execute(get_score,[(usID)])
		srows=c.fetchall()
		db.close()
		#converts tuple to use the score
		scolumns=[desc[0] for desc in c.description]
		results=[dict(zip(scolumns,srow)) for srow in srows] #converts into a dictionary
		score=[srow[0] for srow in srows]#accesses the score in db
		curscore=score[0]
		return 3,curscore#if details found->logged in, returns command and current score

def scoring(username,points):#updates score in database
	if username!='':#if the user has logged in
		#open connection to database
		with sqlite3.connect(db_path) as db:
			c=db.cursor()
		#finds the userID
		find_user='SELECT userID FROM user WHERE username=?'
		c.execute(find_user,[(username)])
		rows=c.fetchall()
		#converts tuple to use the userID
		columns=[desc[0] for desc in c.description]
		results=[dict(zip(columns,row)) for row in rows] #converts into a dictionary
		userID=[row[0] for row in rows]#accesses the userID in db
		usID=userID[0]

		#retrives the current score using the userID
		get_score='SELECT curscore FROM scores WHERE userID=?'
		c.execute(get_score,[(usID)])
		srows=c.fetchall()
		#converts tuple to use the score
		scolumns=[desc[0] for desc in c.description]
		results=[dict(zip(scolumns,srow)) for srow in srows] #converts into a dictionary
		score=[srow[0] for srow in srows]#accesses the score in db
		curscore=score[0]

		#updates score
		curscore=curscore+points
		upd_score='UPDATE scores SET curscore=? WHERE userID=?'
		c.execute(upd_score,[(curscore),(usID)])
		db.commit()
		db.close()
		return curscore #so the score can be updated in the gui
	
#testing scoring system -> it works
#username='r'
#points=5
#newscore=scoring(username,points)
#print(newscore)




#retrieving from multiple tables
#with sqlite3.connect("pmg.db") as db:
	#c=db.cursor()
#ret=("SELECT curscore FROM scores WHERE userID IN (SELECT userID FROM user WHERE username='test_user')")
#c.execute(ret)
#results=c.fetchall()
#print(results)