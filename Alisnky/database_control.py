from DataBase import *
from bs4 import BeautifulSoup
import os

database = database()

while 1:
	print("\nWhat do you wanna do?\n")
	print("1 Write new gesture") 
	print("2 Show all gestures") 
	print("3 Delete a gesture")
	print("4 Exit\n")
	code = input(">")
	try:
		code = int(code)
	except ValueError:
		code = 0

	if code == 1:

		file_name = input("File name>")

		if not os.path.exists(file_name):
			print("\nFile is missing!")
			exit()

		gesture_name = input("Gesture name>")

		if database.get_gesture_id(gesture_name):
			print("\nSuch a gesture already exists!")
			replace = input("Replace?(y/n)>")
			if replace in ["N", "n"]:
				exit()
			else:
				database.del_gesture(TITLE, gesture_name)

		file = open(file_name, 'r')
		soup = BeautifulSoup(file, 'lxml')
		answer1 = soup.select("animation")

		database.write_gesture(gesture_name)

		gesture_id = database.get_gesture_id(gesture_name)

		error = {'arm_l_rotation_euler_X': 19.75554 - 200,
				 'arm_l_rotation_euler_Y': 13.4428 - 150,
				 'arm_r_rotation_euler_X': -19.61401 - 100,
				 'arm_r_rotation_euler_Y': 374.7621 - 150,
				 'head_rotation_euler_X': 0.0 - 150,
				 'head_rotation_euler_Z': 0.0 - 150}

		x_error = -0.01483
		y_error = -0.194612
		x_k = 50 / 0.052466
		y_k = 50 / 0.040542

		for i in range(len(answer1)):
			ID = answer1[i].attrs['id']
			print("\nid =", ID)
			answer2 = answer1[i].select("source")

			for j in range(len(answer2)):
				name = answer2[j].technique_common.accessor.param.attrs['name']
				if name == "TIME":
					temp = str(answer2[j].float_array.string)
					print(name, "=", temp)
				elif name != "INTERPOLATION":
					temp = str(answer2[j].float_array.string)
					print(name, "=", temp)

			if ID in ["arm_l_rotation_euler_X", "arm_l_rotation_euler_Y", 
					  "arm_r_rotation_euler_X", "arm_r_rotation_euler_Y", 
					  "head_rotation_euler_X", "head_rotation_euler_Z"]:
				temp = str(answer2[0].float_array.string)
				tp = [int(round(float(x) * 1000)) for x in temp.split()]
				temp = str(answer2[1].float_array.string)
				angels = [float(x) - error[ID] for x in temp.split()]
				DB_M_id = database.convert_part(ID)
				for j in range(len(tp)):
					database.write_motion(DB_M_id, gesture_id, angels[j], tp[j])
					print("DB>", DB_M_id, gesture_id, angels[j], tp[j])
			elif ID == "eyes_location_X":
				temp = str(answer2[0].float_array.string)
				eyes_tp = [int(round(float(x) * 1000)) for x in temp.split()]
				temp = str(answer2[1].float_array.string)
				x = [float(x) for x in temp.split()]
				print("TP", eyes_tp)
				print("X", x)
			elif ID == "eyes_location_Z":
				temp = str(answer2[0].float_array.string)
				eyes_tp = [int(round(float(x) * 1000)) for x in temp.split()]
				temp = str(answer2[1].float_array.string)
				y = [float(x) for x in temp.split()]
				print("TP", eyes_tp)
				print("Y", y)

		print("\nEyes data:")
		for i in range(len(eyes_tp)):
			database.write_eyes(gesture_id, x[i] - x_error, y[i] - y_error, eyes_tp[i])
			print("DB>", gesture_id, x[i], y[i], eyes_tp[i])

		print("\nData of gesture =", database.gesture(gesture_name))
		print("\nData of eyes =", database.eyes(gesture_name))

		print("\nCompleted!")
	elif code == 2:
		print("\nData:")
		data = database.all_gestures()
		for i in range(len(data)):
			print(data[i][0], data[i][1])
	elif code == 3:
		gesture = input("\nGesture name or id>")
		try:
			gesture = int(gesture)
			if database.get_gesture_title(gesture):
				database.del_gesture(ID, gesture)
				database.del_eyes(gesture)
				print("\nCompleted!")
			else:
				print("\nSuch gesture doesn't exist!")
		except ValueError:
			if database.get_gesture_id(gesture):
				database.del_gesture(TITLE, gesture)
				database.del_eyes(database.get_gesture_id(gesture))
				print("\nCompleted!")
			else:
				print("\nSuch gesture doesn't exist!")
	elif code == 4:
		print("\n====================")
		exit()
	else:
		print("\nInput error!")
	print("\n====================")