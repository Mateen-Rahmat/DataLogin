import sqlite3

db = sqlite3.connect('database.db')
db.commit()


db.execute('INSERT INTO Login VALUES ("Mateen", "Matt123");')
db.commit()

print ("Records are Recorded")