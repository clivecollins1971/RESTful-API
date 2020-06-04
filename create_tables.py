import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)


create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(create_table)


select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

select_query = "SELECT * FROM items"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()

