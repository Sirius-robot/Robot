import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# таблица хранения id и названия жестов
cursor.execute("""CREATE TABLE gestures
                  (gesture_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT)
               """)

# таблица хранения движений для жестов. Привязана к таблице жестов.
cursor.execute("""CREATE TABLE motions
                  (motion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  motor_id INTEGER, gesture_id INTEGER,
                  angel INTEGER, timepoint INTEGER)
               """)


# Таблица конвертации
cursor.execute("""CREATE TABLE conversion
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   DB INTEGER, robot INTEGER, part TEXT, axis TEXT)
               """)

# данные для конвертации
mas = [(1, 1, 'left hand', 'X'), 	(2, 2, 'left hand', 'Y'),
       (3, 3, 'right hand', 'X'), 	(4, 4, 'right hand', 'Y'),
       (5, 5, 'had', 'X'), 			(6, 6, 'had', 'Z')]
cursor.executemany("INSERT INTO conversion (DB, robot, part, axis) VALUES (?,?,?,?)", mas)


# таблица хранения эмоций (не доделано)
cursor.execute("""CREATE TABLE emotions
                  (emotion_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title text)
               """)

conn.commit()

print("Complete!")