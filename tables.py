import sqlite3, os
if not os.path.isfile("pmg.db"):
    db=sqlite3.connect("pmg.db")
    c=db.cursor()

    #creates user table then populates it
    c.execute('''CREATE TABLE IF NOT EXISTS user(
            userID INTEGER PRIMARY KEY NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL);''')
    c.execute('INSERT INTO user(username, password) VALUES ("test_user","MrBob")')
    accounts=[('rattycabbage1','LiLLi43'),('stevenrawn','SR_22j'),('grace315','qwerty')]
    c.executemany('INSERT INTO user(username, password) VALUES(?,?)',accounts)
    db.commit()
    print(c.fetchall())

    #creates object table then populates it
    c.execute('''CREATE TABLE IF NOT EXISTS objects(
    objectID INTEGER PRIMARY KEY NOT NULL,
    object VARCHAR(20) NOT NULL,
    points INTEGER NOT NULL);
    ''')
    obj=[('tennis ball',50),('basketball',25),('shuttlecock',100)]
    c.executemany('INSERT INTO objects(object, points) VALUES(?,?)',obj)
    db.commit()

    #creates score table then populates it
    c.execute('''CREATE TABLE IF NOT EXISTS scores(
    scoreID INTEGER PRIMARY KEY NOT NULL,
    userID INTEGER NOT NULL,
    curscore INTEGER NOT NULL,
    FOREIGN KEY(userID) REFERENCES user(userID));
    ''')
    ascore=[(1,50),(3,550),(2,100)]
    c.executemany('INSERT INTO scores(userID, curscore) VALUES(?,?)',ascore)
    db.commit()

    db.close()
    