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
		cursor.execute(sql, [(motor_id), (gesture_id), (angel), (timepoint), (motion_id)] )
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

	# финальная функция, возвращает информацию о запрашиваемом жесте в необходимом формате (4х мерный список)
	# gesture('smile')
	# [[40, [[1, 180, 0], [3, 90, 0]]], [80, [[1, 32, 0]]], [100, [[2, 180, 0]]]]
	def gesture(self, title):
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

	def gesture2(self, title):
		sql = "SELECT * FROM motions WHERE gesture_id = ? ORDER BY motor_id, timepoint"
		cursor.execute(sql, [(self.get_gesture_id(title))])
		answer = cursor.fetchall()

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
			temp.append(answer[i][1]) # motor_id
			temp.append(answer[i][3]) # angel
			temp.append(m_tp[answer[i][1] - 1][j]) # time
			temp.append(answer[i][4] - temp[2]) # time point
			print(i, 'temp =', temp)
			new_answer.append(temp)
		print('\nnew answer =', new_answer)

		###############################

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
		print('\nstructure of data =', data)
		print('\nM =', m)

		###############################

		return answer

	# Функция конвертации id мотора из базы данных
	# convert motor id of DB to motor id of robot
	# convert(3)
	def convert(self, db_motor_id):
		sql = "SELECT * FROM conversion WHERE DB = ?"
		cursor.execute(sql, [(db_motor_id)])
		return cursor.fetchone()[2]

	# Сообщает всю информацию о моторе из БД (из таблицы конвертации)
	# get_conversion_info(3)
	# id, motor id of DB, motor id of robot, part of robot, rotation axle
	# (3, 3, 3, 'right hand', 'X')
	def get_conversion_info(self, db_motor_id):
		sql = "SELECT * FROM conversion WHERE DB = ?"
		cursor.execute(sql, [(db_motor_id)])
		return cursor.fetchone()

	def new_conversion_table(self):
		sql = "DROP TABLE conversion"
		cursor.execute(sql)
		conn.commit()
		cursor.execute("""CREATE TABLE conversion
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   DB INTEGER, robot INTEGER, part TEXT, axis TEXT)
               	   """)

		# данные для конвертации
		mas = [(1, 1, 'left hand', 'X'), 	(2, 2, 'left hand', 'Y'),
       		   (3, 3, 'right hand', 'X'), 	(4, 4, 'right hand', 'Y'),
       		   (5, 5, 'had', 'X'), 			(6, 6, 'had', 'Z')]

		cursor.executemany("INSERT INTO conversion (DB, robot, part, axis) VALUES (?,?,?,?)", mas)
		conn.commit()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
database = database()

################################################################################
# конец библиотеки и начало программы тестов

gesname = 'smail'

# записываем в БД новый жест и 4 движения для него
database.write_gesture(gesname)
database.write_motion(1, database.get_gesture_id(gesname), 180, 40)
database.write_motion(2, database.get_gesture_id(gesname), 180, 100)
database.write_motion(3, database.get_gesture_id(gesname), 90, 20)
database.write_motion(3, database.get_gesture_id(gesname), 45, 40)
database.write_motion(1, database.get_gesture_id(gesname), 32, 100)
database.write_motion(6, database.get_gesture_id(gesname), 125, 69)

# выводим записанную информацию для проверки
print(database.get_gesture(gesname))

# выводим данные по жесту в необходимом нам формате
print('\nfinal data =', database.gesture2(gesname))

# удоляем жест и привязанные к нему движения 
database.del_gesture(TITLE, gesname)

print('First test is OK!\n')

# проверяем конвертацию id моторов
print('info of conversion', database.get_conversion_info(3))
print('convert', database.convert(1))

print('Second test is OK!\n')

# проверяем перезапись таблицы конвертации
database.new_conversion_table()
print('info of new conversion', database.get_conversion_info(3))

print('Third test is OK!\n')