from bs4 import BeautifulSoup
from DataBase import *
file_name = input("File name>")
gesture_name = input("Gesture name>")
file = open(file_name, 'r')
soup = BeautifulSoup(file, 'lxml')
answer1 = soup.select("animation")
database.write_gesture(gesture_name)

# l_arm_X
# l_arm_Y
# r_arm_X
# r_arm_Y
# head_X
# head_Z
error = [19.75554, 13.4428, -19.61401, 374.7621, 0, 0]

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
		angels = [float(x) for x in temp.split()]
		DB_M_id = database.convert_part(ID)
		gesture_id = database.get_gesture_id(gesture_name)
		for j in range(len(tp)):
			database.write_motion(DB_M_id, gesture_id, angels[j], tp[j])
			print("DB>", DB_M_id, gesture_id, angels[j], tp[j])
	elif ID == "eyes_location_X":
		print("NO DATA!")
	elif ID == "eyes_location_Z":
		print("NO DATA!")

print("\nComplate!")

print("\nData =", database.gesture(gesture_name))

#database.del_gesture(TITLE, gesture_name)