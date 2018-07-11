import sqlite3
ID = 1
TITLE = 0
class database:

	# запись нового движения для жеста
	# write_motion(5, 11, 180, 40)
	def write_motion(self, motor_id, gesture_id, angel, timepoint):
		sql = """INSERT INTO motions 
		(motor_id, gesture_id, angel, timepoint) 
		VALUES (?, ?, ?, ?)"""
		cursor.execute(sql, [(motor_id), (gesture_id), (angel), (timepoint)])
		conn.commit()

	# удаление движения по его id
	# del_motion(11)
	def del_motion(self, motion_id):
		sql = "DELETE FROM motions WHERE motion_id = ?"
		cursor.execute(sql, [(motion_id)])
		conn.commit()

	# изменяет значения одной записи из таблици движений
	# 
	def change_motion(self, motion_id, motor_id, gesture_id, angel, timepoint):
		sql = """UPDATE motions 
			SET motor_id = ?, gesture_id = ?, angel = ?, timepoint = ?
			WHERE motion_id = ?"""
		cursor.execute(sql, [(motor_id)], [(gesture_id)], [(angel)], [(timepoint)], [(motion_id)] )
		conn.commit()

	# возвращает запись движения по id
	# get_motion(11)
	def get_motion(self, motion_id):
		sql = "SELECT * FROM motions WHERE motion_id = ?"
		cursor.execute(sql, [(motion_id)])
		return cursor.fetchone()

	# запись нового жеста
	# write_gesture('smile'):
	def write_gesture(self, title):
		sql = "INSERT INTO gestures (title) VALUES (?)"
		cursor.execute(sql, [(title)])
		conn.commit()

	# удаление жеста и всех привязанных к нему движений
	# del_gesture(TITLE, 'smile')
	def del_gesture(self, idti, where):
		if idti:
			sql1 = "DELETE FROM gestures WHERE gesture_id = ?"
			sql2 = "DELETE FROM motions WHERE gesture_id = ?"
			cursor.execute(sql2, [(where)])
		else:
			sql1 = "DELETE FROM gestures WHERE title = ?"
			sql2 = "DELETE FROM motions WHERE gesture_id = ?"
			cursor.execute(sql2, [(self.get_gesture_id(where))])
		cursor.execute(sql1, [(where)])
		conn.commit()

	# изменение названия жеста и всех привязанных к нему движений по id или по названию
	# change_gesture(ID, 'smile', 11)
	def change_gesture(self, idti, what, where):
		if idti:
			sql = """UPDATE gestures 
			SET title = ? 
			WHERE gesture_id = ?"""
		else:
			sql = """UPDATE gestures 
			SET title = ? 
			WHERE title = ?"""
		cursor.execute(sql, [(what)], [(where)])
		conn.commit()

	# возвращает id жеста по названию
	# get_gesture_id('smile')
	def get_gesture_id(self, title):
		sql = "SELECT * FROM gestures WHERE title = ?"
		cursor.execute(sql, [(title)])
		return cursor.fetchall()[0][0]

	# возвращает всю информацию о жесте по названию
	# get_gesture('smile')
	def get_gesture(self, title):
		sql = "SELECT * FROM motions WHERE gesture_id = ? ORDER BY timepoint"
		cursor.execute(sql, [(self.get_gesture_id(title))])
		answer = cursor.fetchall()
		return answer

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
database = database()