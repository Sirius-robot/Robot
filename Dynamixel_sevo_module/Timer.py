import servocontrol
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

def slaver():
    time_dict = q.get()
    servocontrol.multiInt((1, 2, 3, 4, 5, 6))
   # servocontrol.robotControl((1,2,4,5,6),(400,1000,200,500,500),(300,300,300,300,30))
    print(time_dict)
    def work():
        global time_iter
        time_iter += 10
        return time_iter

    def timer1():
        global lenni
        threading.Timer(0.04, timer1).start()
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
            servocontrol.robotControl(data[0], data[2], data[1])
    timer1()

