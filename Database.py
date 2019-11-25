import sqlite3

db = sqlite3.connect('database.db')
db.commit()
print ("Database Created")

db.execute('CREATE TABLE Login (USERNAME TEXT, PASSWORD TEXT)')
print ("Table Created")
db.commit()

