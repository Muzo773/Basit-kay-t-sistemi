import sqlite3
isim = str(input("Lütfen İsminizi Giriniz    : "))
soyisim = str(input("Lütfen Soyisminizi Giriniz : "))
conn = sqlite3.connect('data_base.sql')

cursor = conn.cursor()

cursor.execute("INSERT INTO deneme (isim, soyisim) VALUES (?, ?)", (isim, soyisim))

conn.commit()