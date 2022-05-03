import sqlite3

yaihDB = sqlite3.connect("api/db/yaih.db")
yaih = yaihDB.cursor()

yaih.execute("CREATE TABLE users (id INTEGRER PRIMARY KEY, key TEXT, domain TEXT)")
yaih.execute("CREATE TABLE images (id TEXT PRIMARY KEY, url TEXT, del TEXT, owner INTEGRER, pathName TEXT)")

yaihDB.commit()
yaihDB.close()