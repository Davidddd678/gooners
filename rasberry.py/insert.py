import sqlite3

connection = sqlite3.connect("db.sqlite")

cursor = connection.cursor()

command= "INSERT INTO User (login, password) VALUES(?, ?)"
data = ("miaw","123")

cursor.execute(command, data)

connection.commit()

connection.close()

print("Goon!")