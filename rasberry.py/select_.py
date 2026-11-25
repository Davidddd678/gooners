import sqlite3

connection = sqlite3.connect("db.sqlite")

cursor = connection.cursor()

command= "SELECT * FROM User WHERE login = ? AND password = ?"
data=("admin","123")


cursor.execute(command,data)

users = cursor.fetchall()

for user in users:
    print(user)

connection.commit()

connection.close()

print("Goon!")