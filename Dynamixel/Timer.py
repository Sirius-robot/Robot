import threading
import sys
import time
import queue
sys.path.insert(3, 'Dynamixel_sevo_module')
from servocontrol import *
import Timer
import choose_behavior
sys.path.insert(0, 'Alisnky')
from DataBase import *
#sys.path.insert(1, 'Sinthesis')
#from sinthesis import *
sys.path.insert(2, 'recognition')
from parsing_bml import *

global max_time_val

max_time_val = 0
time_iter = -40
lenni = 0

def timer(chbh_to_timer,timer_to_images,timer_to_eyepos,event):
    multiInt((1, 2, 3, 4, 5, 6))
    def work():
        global time_iter
        time_iter += 40
        return time_iter
    def timer1():
        threading.Timer(0.04, timer1).start()
        global time_iter
        global max_time_val
        global anglea
        global datauy
        global time_dict
        if time_dict == None:
            if not chbh_to_timer.empty():
                big_dict = chbh_to_timer.get()
                if 'img_mouth' in big_dict:
                    mouth = big_dict['img_mouth']
                if 'img_brows' in big_dict:
                    brows = big_dict['img_brows']
                if 'pupils' in big_dict:
                    pupils = big_dict['pupils']
                timer_to_images.put([brows[0], mouth[0], int(pupils[0])])
                if 'command_eye' in big_dict:
                    command_eye = big_dict['command_eye']

                print('start')
                if 'command_motor' in big_dict:
                    time_dict = big_dict['command_motor']
                    print("time_dict")
                    global datauy
                    datauy = time_dict[-2]
                    anglea = multiread([1, 2, 3, 4, 5, 6])
                    for z in range(len(datauy[0])):
                        datauy[2][z] = datauy[1][z]/1024*300
                    robotControl(datauy[0], datauy[2], datauy[1], anglea)
                    for i in range(len(datauy[0])):
                        anglea[datauy[0][i]] = datauy[1][i]
        else:
            d = work()
            if d > max_time_val:
                max_time_val = 0
                time_iter = -40
                time_dict = None
                event.set()
            
            if time_dict != None:
                if time_dict.get(d, -666) != -666:

                    datauy = time_dict[d]
                    for y in datauy[2]:
                        if y + d > max_time_val:
                            max_time_val = y + d
                    print(datauy[0])
                    print(datauy[2])
                    robotControl(datauy[0], datauy[2], datauy[1], anglea)
                    print('Sent')
                    for i in range(len(datauy[0])):
                        anglea[datauy[0][i]] = datauy[1][i]
    global time_dict
    time_dict = None
    timer1()
