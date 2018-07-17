from DataBase import *

database = database()

gesname = 'smail'

# записываем в БД новый жест и 4 движения для него
database.write_gesture(gesname)
database.write_motion(1, database.get_gesture_id(gesname), 180.0, 40)
database.write_motion(2, database.get_gesture_id(gesname), 180.0, 100)
database.write_motion(3, database.get_gesture_id(gesname), 90.0, 20)
database.write_motion(3, database.get_gesture_id(gesname), 45.0, 40)
database.write_motion(1, database.get_gesture_id(gesname), 32.0, 100)
database.write_motion(6, database.get_gesture_id(gesname), 125.0, 69)

# выводим данные по жесту в необходимом нам формате
print('\nData =', database.gesture(gesname))

# удfляем жест и привязанные к нему движения 
database.del_gesture(TITLE, gesname)