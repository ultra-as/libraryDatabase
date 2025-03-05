import sqlite3 as sql

db = sql.connect("library.db")

c = db.cursor()
c.execute("DROP TABLE IF EXISTS users")
c.execute("CREATE TABLE users (username TEXT PRIMARY KEY, password, firstname, lastname)")

f = open("users.csv","r")
for line in f.readlines():
    bits = line.strip().split(",")
    c.execute("INSERT INTO users VALUES (?,?,?,?)", bits)
db.commit()

