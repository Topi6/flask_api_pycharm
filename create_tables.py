import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"

cursor.execute(create_table_users)
cursor.execute(create_table_items)

#cursor.execute("INSERT INTO items VALUES ('test_item', 15.34)")

connection.commit()

connection.close()