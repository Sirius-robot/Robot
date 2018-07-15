import botcontrol
import threading
import sys
sys.path.insert(0, '../Alisnky')
from DataBase import *
command_data = database.gesture('smail')
time_iter = -10

time_dict = {}

#database.del_gesture(TITLE, gesname)
for commands_time in command_data:
    time = commands_time[0]
    commands = commands_time[1]
    ids = []
    angles = []
    dif_times = []
    for command in commands:
        ids.append(command[0])
        angles.append(command[1])
        dif_times.append(command[2])
        time_dict[time] = [ids, angles, dif_times]
#database.del_gesture(TITLE, gesname)
#print(time_dict)
botcontrol.multiInt(ids)

#botcontrol.multiInt((1,2,3,4,5,6))
#botcontrol.robotControl((1,2,3,5,6),(200,400,1000,200,500),(200,300,300,300,300,30))
lenni=0
def work():
    global time_iter
    time_iter += 10
    return time_iter

def timer1():
    global lenni
    threading.Timer(0.01,timer1).start()
    d = work()
    lenny = len(time_dict.keys())
    if lenny == lenni:
        print('THE END')
        lenni+=1
    if time_dict.get(d,666) != 666:
        lenni = lenni + 1
        data = time_dict[d]
        print(time_dict.get(d))
        print(data[0])
        print(data[2])
        print(data[1])
        botcontrol.robotControl(data[0],data[2],data[1])

#database.del_gesture(TITLE, gesname)
timer1()
