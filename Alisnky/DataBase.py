import sqlite3
ID = 1
TITLE = 0
class database:
	def __init__(self):
		self.conn = sqlite3.connect("database.db")
		self.cursor = self.conn.cursor()

	def write_motion(self, motor_id, gesture_id, angel, timepoint):
		"""
		запись нового движения для жеста
		write_motion(5, 11, 180, 40)
		"""
		sql = """INSERT INTO motions 
		(motor_id, gesture_id, angel, timepoint) 
		VALUES (?, ?, ?, ?)"""
		self.cursor.execute(sql, [(motor_id), (gesture_id), (angel), (timepoint)])
		self.conn.commit()

	def del_motion(self, motion_id):
		"""
		удаление движения по его id
		del_motion(11)
		"""
		sql = "DELETE FROM motions WHERE motion_id = ?"
		self.cursor.execute(sql, [(motion_id)])
		self.conn.commit()

	def change_motion(self, motion_id, motor_id, gesture_id, angel, timepoint):
		"""
		изменяет значения одной записи из таблици движений
		"""
		sql = """UPDATE motions 
			SET motor_id = ?, gesture_id = ?, angel = ?, timepoint = ?
			WHERE motion_id = ?"""
		self.cursor.execute(sql, [(motor_id), (gesture_id), (angel), (timepoint), (motion_id)] )
		self.conn.commit()

	def get_motion(self, motion_id):
		"""
		возвращает запись движения по id
		get_motion(11)
		"""
		sql = "SELECT * FROM motions WHERE motion_id = ?"
		self.cursor.execute(sql, [(motion_id)])
		return self.cursor.fetchone()

	def write_gesture(self, title):
		"""
		запись нового жеста
		write_gesture('smile'):
		"""
		sql = "INSERT INTO gestures (title) VALUES (?)"
		self.cursor.execute(sql, [(title)])
		self.conn.commit()

	def del_gesture(self, idti, where):
		"""
		удаление жеста и всех привязанных к нему движений по id или по названию
		del_gesture(TITLE, 'smile')
		"""
		if idti:
			sql1 = "DELETE FROM gestures WHERE gesture_id = ?"
			sql2 = "DELETE FROM motions WHERE gesture_id = ?"
			self.cursor.execute(sql2, [(where)])
		else:
			sql1 = "DELETE FROM gestures WHERE title = ?"
			sql2 = "DELETE FROM motions WHERE gesture_id = ?"
			self.cursor.execute(sql2, [(self.get_gesture_id(where))])
		self.cursor.execute(sql1, [(where)])
		self.conn.commit()

	def change_gesture(self, idti, what, where):
		"""
		Изменение названия жеста по id или по названию
		change_gesture(ID, 'smile', 11)
		"""
		if idti:
			sql = """UPDATE gestures 
			SET title = ? 
			WHERE gesture_id = ?"""
		else:
			sql = """UPDATE gestures 
			SET title = ? 
			WHERE title = ?"""
		self.cursor.execute(sql, [(what), (where)])
		self.conn.commit()

	def all_gestures(self):
		sql = "SELECT * FROM gestures"
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def get_gesture_id(self, title):
		"""
		Возвращает id жеста по его названию
		get_gesture_id('smile')
		"""
		sql = "SELECT * FROM gestures WHERE title = ?"
		self.cursor.execute(sql, [(title)])
		answer = self.cursor.fetchone()
		if answer: 
			return answer[0]
		else:
			return 0

	def get_gesture_title(self, gesture_id):
		"""
		Возвращает название жеста по его id
		get_gesture_title(11)
		"""
		sql = "SELECT * FROM gestures WHERE gesture_id = ?"
		self.cursor.execute(sql, [(gesture_id)])
		answer = self.cursor.fetchone()
		if answer:
			return answer[1]
		else:
			return 0

	def get_gesture(self, title):
		"""
		Возвращает всю информацию о жесте по названию
		get_gesture('smile')
		"""
		sql = "SELECT * FROM motions WHERE gesture_id = ? ORDER BY timepoint"
		self.cursor.execute(sql, [(self.get_gesture_id(title))])
		answer = self.cursor.fetchall()
		return answer

	def gesture_without_tp(self, title):
		"""
		Финальная функция, но временные точки не начала, а конца движений
		gesture_without_tp('smile')
		example:
		[[40, [[1, 180, 0], [3, 90, 0]]], [80, [[1, 32, 0]]], [100, [[2, 180, 0]]]]
		"""
		answer = self.get_gesture(title)
		count_tp = 0
		temp = -1
		motors = []
		tp = []
		m = [[0], [0], [0], [0], [0], [0]]
		for i in range(len(answer)):
			if temp != answer[i][4]:
				count_tp += 1
				temp = answer[i][4]
				motors.append(1)
				tp.append(answer[i][4])
			else:
				motors[count_tp - 1] += 1
			m[answer[i][1] - 1].append(answer[i][4])
		data = [[0, 0] for data in range(count_tp)]
		for i in range(count_tp):
			temp = []
			for j in range(motors[i]):
				temp.append([0, 0, 0])
			data[i][1] = temp
		print('structure of data', data)
		print('M -', m)

		temp = 0
		mi = [0, 0, 0, 0, 0, 0]
		for i in range(count_tp):
			data[i][0] = tp[i]
			for j in range(motors[i]):

				data[i][1][j][0] = self.convert(answer[temp][1])
				data[i][1][j][1] = answer[temp][3]

				a = data[i][1][j][0]
				data[i][1][j][2] = m[a - 1][mi[a - 1] + 1] - m[a - 1][mi[a - 1]] 
				mi[a - 1] += 1

				temp += 1

		return data

	def gesture(self, title):
		"""
		Финальная функция, возвращает информацию о запрашиваемом жесте в 
		необходимом формате (4х мерный список)
		gesture('smile')
		data:
		[[0, [[1, 180, 40], [2, 180, 100], [3, 90, 20], [6, 125, 69]]], 
		[20, [[3, 45, 20]]], [40, [[1, 32, 60]]]]
		"""

		# Запрашиваем необходимые нам данные и преобразуем их в удобный нам, 
		# промежуточный формат (new_answer)
		
		sql = "SELECT * FROM motions WHERE gesture_id = ? ORDER BY motor_id, timepoint"
		self.cursor.execute(sql, [(self.get_gesture_id(title))])
		answer = self.cursor.fetchall()

		m_tp = [[], [], [], [], [], []]
		temp = 0

		for i in range(len(answer)):
			if answer[i][1] == answer[i - 1][1]:
				m_tp[answer[i][1] - 1].append(answer[i][4] - answer[i - 1][4])
			else:
				m_tp[answer[i][1] - 1].append(answer[i][4])
		new_answer = []
		j = 0
		for i in range(len(answer)):
			if answer[i][1] == answer[i - 1][1]: j += 1
			else: j = 0 
			temp = []
			temp.append(answer[i][1]) 				# motor_id
			temp.append(answer[i][3]) 				# angel
			temp.append(m_tp[answer[i][1] - 1][j]) 	# time
			temp.append(answer[i][4] - temp[2]) 	# time point
			new_answer.append(temp)
		new_answer.sort(key=lambda i: i[3]) #преобразованные данные, промежуточный список

		# Генерируем необходимую нам структуру списка

		count_tp = 0
		temp = -1
		motors = []
		tp = []
		for i in range(len(new_answer)):
			if temp != new_answer[i][3]:
				count_tp += 1
				temp = new_answer[i][3]
				motors.append(1)
				tp.append(new_answer[i][3])
			else:
				motors[count_tp - 1] += 1
		data = [[0, 0] for data in range(count_tp)]
		for i in range(count_tp):
			temp = []
			for j in range(motors[i]):
				temp.append([0, 0, 0])
			data[i][1] = temp

		# Заполняем структуру данными

		temp = 0
		for i in range(count_tp):
			data[i][0] = tp[i]
			for j in range(motors[i]):

				data[i][1][j][0] = self.convert(new_answer[temp][0])
				data[i][1][j][1] = new_answer[temp][1]

				data[i][1][j][2] = new_answer[temp][2]				

				temp += 1

		return data

	def convert(self, db_motor_id):
		"""
		Функция конвертации id мотора из базы данных
		convert motor id of DB to motor id of robot
		convert(3)
		"""
		sql = "SELECT * FROM conversion WHERE DB = ?"
		self.cursor.execute(sql, [(db_motor_id)])
		return self.cursor.fetchone()[2]

	def convert_part(self, part):
		"""
		Функция конвертации названия части тела в id необходимого мотора в бд
		"""
		sql = "SELECT * FROM conversion WHERE part = ?"
		self.cursor.execute(sql, [(part)])
		return self.cursor.fetchone()[0]

	def get_conversion_info(self, db_motor_id):
		"""
		Сообщает всю информацию о моторе из БД (из таблицы конвертации)
		get_conversion_info(3)
		data format:
		id, motor id of DB, motor id of robot, part of robot, rotation axle
		data:
		(3, 3, 3, 'right hand', 'X')
		"""
		sql = "SELECT * FROM conversion WHERE DB = ?"
		self.cursor.execute(sql, [(db_motor_id)])
		return self.cursor.fetchone()

	def get_all_conversion_info(self):
		"""
		Сообщает всю информацию из таблицы конвертации
		"""
		sql = "SELECT * FROM conversion"
		self.cursor.execute(sql)
		return self.cursor.fetchall()

	def new_conversion_table(self):
		"""
		Удаляет и создаёт новую таблицу конвертации. Нужна для изменения данных.
		Данные необходимо вводить в самом теле процедуры в списке mas.
		формат:
		id мотора в БД, id мотора в роботе, часть тела, ось вращения
		"""
		sql = "DROP TABLE conversion"
		self.cursor.execute(sql)
		self.conn.commit()
		self.cursor.execute("""CREATE TABLE conversion
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

		self.cursor.executemany("INSERT INTO conversion (DB, robot, part, axis) VALUES (?,?,?,?)", mas)
		self.conn.commit()

	def write_eyes(self, gesture_id, x, y, tp):
		"""
		Запись нового движения зрачков.
		Необходимо указать id жеста, x и y куда нужно переместить зрачки, 
		и временную точку.
		"""
		sql = """INSERT INTO eyes 
		(gesture_id, x, y, timepoint) 
		VALUES (?, ?, ?, ?)"""
		self.cursor.execute(sql, [(gesture_id), (x), (y), (tp)])
		self.conn.commit()

	def del_eyes(self, gesture_id):
		"""
		Удоляет все движения глаз привязанные к определённому id жеста.
		"""
		sql = "DELETE FROM eyes WHERE gesture_id = ?"
		self.cursor.execute(sql, [(gesture_id)])
		self.conn.commit()

	def get_eyes(self, gesture_id):
		"""
		Возвращает всю информацию о движениях глаз по id жеста к которому 
		они привязаны.
		Example:
		[(1, 3, 7.0, 5.0, 80), (2, 3, 10.0, 10.0, 140), 
		(3, 3, -400.0, 1000.0, 1000), (4, 3, 6.0, 5.0, 50), 
		(5, 3, 10.0, 10.0, 69)]
		"""
		sql = "SELECT * FROM eyes WHERE gesture_id = ? ORDER BY timepoint"
		self.cursor.execute(sql, [(gesture_id)])
		return self.cursor.fetchall()

	def eyes(self, title):
		"""
		Возвращает информацию по движению глаз по названию жеста.
		Example:
		[[80, -0.01006066, -0.1946116], [1200, -0.005579948, -0.1804265], 
		[2400, -0.01006066, -0.1946116]]
		"""
		answer = self.get_eyes(self.get_gesture_id(title))
		data = []

		tp = [0]
		for i in range(len(answer)):
			tp.append(answer[i][4])

		for i in range(len(answer)):
			temp = []
			temp.append(tp[i]) # Time point
			temp.append(answer[i][2]) # X
			temp.append(answer[i][3]) # Y
			temp.append(tp[i + 1] - tp[i]) # Time
			data.append(temp)
		return data

# self.conn = sqlite3.self.connect("database.db")
# self.cursor = self.conn.self.cursor()
# database = database()

################################################################################
# конец библиотеки