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

	def gesture(self, title):
		answer = self.get_gesture(title)
		count_tp = 0
		temp = -1
		motors = []
		tp = []
		indices = []
		angles = []
		# m1 = []
		# m2 = []
		# m3 = []
		# m4 = []
		# m5 = []
		# m6 = []
		for i in range(len(answer)):
			if temp != answer[i][4]:
				count_tp += 1
				temp = answer[i][4]
				motors.append(1)
				tp.append(answer[i][4])
			else:
				motors[count_tp - 1] += 1
		data = [[0, 0] for data in range(count_tp)]
		for i in range(count_tp):
			temp = []
			for j in range(motors[i]):
				temp.append([0, 0, 0])
			data[i][1] = temp
		print('structure of data', data)

		temp = 0
		for i in range(count_tp):
			data[i][0] = tp[i]
			for j in range(motors[i]):
				data[i][1][j][0] = self.convert(answer[temp][1])
				data[i][1][j][1] = answer[temp][3]
				temp += 1

		return data

	def convert(self, db_motor_id):
		sql = "SELECT * FROM conversion WHERE DB = ?"
		cursor.execute(sql, [(db_motor_id)])
		return cursor.fetchone()[2]

	def get_conversion_info(self, db_motor_id):
		sql = "SELECT * FROM conversion WHERE DB = ?"
		cursor.execute(sql, [(db_motor_id)])
		return cursor.fetchone()



conn = sqlite3.connect("database.db")
cursor = conn.cursor()
database = database()

gesname = 'smail'

database.write_gesture(gesname)
database.write_motion(1, database.get_gesture_id(gesname), 180, 40)
database.write_motion(2, database.get_gesture_id(gesname), 180, 100)
database.write_motion(3, database.get_gesture_id(gesname), 90, 40)
database.write_motion(1, database.get_gesture_id(gesname), 32, 80)

print(database.get_gesture(gesname))

print('final data', database.gesture(gesname))

database.del_gesture(TITLE, gesname)

print('First test is OK!\n')

print('info of conversion', database.get_conversion_info(5))
print('convert', database.convert(1))

print('Second test is OK')