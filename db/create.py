import sqlite3

yaihDB = sqlite3.connect("db/yaih.db")
yaih = yaihDB.cursor()

yaih.execute("CREATE TABLE images (id INTEGER PRIMARY KEY, url TEXT, del TEXT, owner INTEGRER)")
yaih.execute("CREATE TABLE users (id INTEGRER PRIMARY KEY, key TEXT, url TEXT)")


yaihDB.commit()
yaihDB.close()