import sqlite3

class Actions:
    def __init__(self):
        self.users = "users"
        self.images = "images"
        self.db = sqlite3.connect("api/db/yaih.db")
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.db.close()

    # User

    def addUserDB(self, id, key="", domain=""):
        self.cursor.execute("INSERT OR REPLACE INTO users (id, key, domain) VALUES (?, ?, ?)", (id, key, domain))
        self.db.commit()

    def deleteUserDB(self, id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
        self.db.commit()

    def getDomainDB(self, id):
        self.cursor.execute("SELECT domain FROM users WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def editDomainDB(self, id, domain):
        self.cursor.execute("UPDATE users SET domain=? WHERE id=?", (domain, id))
        self.db.commit()

    def getKeyDB(self, id):
        self.cursor.execute("SELECT key FROM users WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def editKeyDB(self, id, key):
        self.cursor.execute("UPDATE users SET key=? WHERE id=?", (key, id))
        self.db.commit()

    
    # Image

    def addImageDB(self, id, url, del_, owner, path):
        self.cursor.execute("INSERT OR REPLACE INTO images (id, url, del, owner, pathName) VALUES (?, ?, ?, ?, ?)", (id, url, del_, owner, path))
        self.db.commit()

    def deleteImageDB(self, id):
        self.cursor.execute("DELETE FROM images WHERE id=?", (id,))
        self.db.commit()

    def getURLDB(self, id):
        self.cursor.execute("SELECT url FROM images WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def getDeleteDB(self, id):
        self.cursor.execute("SELECT del FROM images WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def getOwnerDB(self, id):
        self.cursor.execute("SELECT owner FROM images WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def getPathDB(self, id):
        self.cursor.execute("SELECT pathName FROM images WHERE id=?", (id,))
        return self.cursor.fetchone()[0]

    def getAllOwnerDB(self, owner):
        self.cursor.execute("SELECT * FROM images WHERE owner=?", (owner,))
        return [x[0] for x in self.cursor.fetchall()]