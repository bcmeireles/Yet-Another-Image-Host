import sqlite3

class Actions:
    def __init__(self):
        self.users = "users"
        self.images = "images"
        self.db = sqlite3.connect("db/yaih.db")
        self.cursor = self.db.cursor()

    def editUser(self, id, key, url):
        self.cursor.execute("INSERT OR REPLACE INTO users (id, key, url) VALUES (?, ?, ?)", (id, key, url))
        self.db.commit()
        self.db.close()

    def deleteUser(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (id,))