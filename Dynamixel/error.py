import botcontrol
import threading
import sys
import queue
from test1 import *
sys.path.insert(0, '../Alisnky')
from DataBase import *

time_iter = -10
def master(q):
    f = open('vvv.bml', 'r')
    z = f.read()
    x = dictionary_result(z)
    print(x[0])
    gestur = x[0]
    command_data = database.gesture(gestur)
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
            time_dict[time] = [ids, angles, dif_times]#очередь 
        q.put(time_dict)

def slaver(q):
    
    def work():
        global time_iter
        time_iter += 10
        return time_iter

    def timer1():
        if not q.empty():
            time_dict = q.get()
        global lenni
        threading.Timer(0.01, timer1).start()
        d = work()
        try:
            lenny = len(time_dict.keys())
            if lenny == lenni:
                print('THE END')
            lenni += 1
            if time_dict.get(d, 666) != 666:
                lenni = lenni + 1
                data = time_dict[d]
                print(time_dict.get(d))
                print(data[0])
                print(data[2])
                print(data[1])
                botcontrol.robotControl(data[0], data[2], data[1])
        except:
           pass
    timer1()
q = queue.Queue()
mastert = threading.Thread(target = master, args = (q,))
mastert.start()
slavert = threading.Thread(target = slaver, args = (q,))
slavert.start()