import botcontrol
import threading
import sys
import time
import queue

sys.path.insert(0, '../Alisnky')
from DataBase import *
sys.path.insert(1, '../Sinthesis')
from sinthesis import *
sys.path.insert(2, '../recognition')
from parsing_bml import *

time_iter = -10
lenni = 0
q = queue.Queue()

def master():

    db = database()
    while 1:
        f = open('vvv.bml', 'r')
        z = f.read()
        x = dictionary_result(z)
        gestur = x['figure']
        texts = x['speech']
        if len(gestur) > 0:
            if len(gestur[0]) > 0:
                command_data = db.gesture(gestur[0])
                time_dict = {}
                for commands_time in command_data:
                    timew = commands_time[0]
                    commands = commands_time[1]
                    ids = []
                    angles = []
                    dif_times = []
                    for command in commands:
                        ids.append(command[0])
                        angles.append(command[1])
                        dif_times.append(command[2])
                        time_dict[timew] = [ids, angles, dif_times]  # очередь
                q.put(time_dict)
        if len(texts) > 0:
            if len(texts[0])>0:
                print(texts[0])
                audio = speech(texts[0])
                winsound.PlaySound(audio, winsound.SND_MEMORY)
        # sinthesis.speech(text)
        #if text =
        time.sleep(5)

def slaver():
    time_dict = q.get()
    botcontrol.multiInt((1, 2, 3, 4, 5, 6))
   # botcontrol.robotControl((1,2,4,5,6),(400,1000,200,500,500),(300,300,300,300,30))
    print(time_dict)
    def work():
        global time_iter
        time_iter += 10
        return time_iter

    def timer1():
        global lenni
        threading.Timer(0.01, timer1).start()
        d = work()
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
    timer1()

mastert = threading.Thread(target=master)
mastert.start()
slavert = threading.Thread(target=slaver)
slavert.start()