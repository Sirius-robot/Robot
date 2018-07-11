import sqlite3

conn = sqlite3.connect("conversion_table.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE table
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   DB INTEGER, robot INTEGER, part TEXT, axis TEXT)
               """)

mas = [(1, 1, 'left hand', 'X'), 	(2, 2, 'left hand', 'Y'),
       (3, 3, 'right hand', 'X'), 	(4, 4, 'right hand', 'Y'),
       (5, 5, 'had', 'X'), 			(6, 6, 'had', 'Z')]

cursor.executemany("INSERT INTO table VALUES (?,?,?,?)", mas)
conn.commit()