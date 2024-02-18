import sqlite3

conn = sqlite3.connect('data_base.sql')
cursor = conn.cursor() 

cursor.execute('''
            CREATE TABLE IF NOT EXISTS deneme(isim TEXT, soyisim TEXT, yas INTEGER)
             ''')

conn.commit()