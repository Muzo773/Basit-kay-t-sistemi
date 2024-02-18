import sqlite3

conn = sqlite3.connect('data_base.sql')

cursor = conn.cursor()

cursor.execute("SELECT * FROM deneme")
rows = cursor.fetchall()

for row in rows:
    print(row)