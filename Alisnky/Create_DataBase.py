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
                  angel REAL, timepoint INTEGER)
               """)


# Таблица конвертации
cursor.execute("""CREATE TABLE conversion
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   DB INTEGER, robot INTEGER, part TEXT, axis TEXT)
               """)

# данные для конвертации
mas =  [(1, 1, 'arm_l_rotation_euler_X', 'X'), 
        (2, 2, 'arm_l_rotation_euler_Y', 'Y'),
        (3, 3, 'arm_r_rotation_euler_X', 'X'), 
        (4, 4, 'arm_r_rotation_euler_Y', 'Y'),
        (5, 5, 'head_rotation_euler_X', 'X'), 
        (6, 6, 'head_rotation_euler_Z', 'Z')]
cursor.executemany("INSERT INTO conversion (DB, robot, part, axis) VALUES (?,?,?,?)", mas)


# таблица движений глаз
cursor.execute("""CREATE TABLE eyes
                  (eyes_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  gesture_id INTEGER, x REAL, y REAL, timepoint INTEGER)
               """)

conn.commit()

print("Completed!")