import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE gestures
                  (gesture_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT)
               """)

cursor.execute("""CREATE TABLE motions
                  (motion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  motor_id INTEGER, gesture_id INTEGER,
                  angel INTEGER, timepoint INTEGER)
               """)

cursor.execute("""CREATE TABLE emotions
                  (emotion_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title text)
               """)

conn.commit()

print("Complete!")