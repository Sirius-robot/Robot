import botcontrol
from DataBase import *
import threading
#database.data[i][1][j][1]
command_data = database.gesture(gesname)
flag = 0
#time_iter=-10
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
database.del_gesture(TITLE, gesname)

botcontrol.multiInt((1,2,3,4))
botcontrol.robotControl((1,2,3,5),(1023,6000,10000,20000),(300,300,300,150))

def timer1():
    threading.Timer(0.01,timer1).start()
    time_iter = time_iter+10
    print(time_iter)
    # if (time == time_iter):
    #    time_dict[time] = [ids,angles,dif_times]
     #   print(time_dict)


timer1()
