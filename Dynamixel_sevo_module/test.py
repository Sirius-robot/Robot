import servocontrol
import threading
import sys
import time
import queue
import choose_behavior
import Timer
sys.path.insert(0, '../Alisnky')
from DataBase import *
sys.path.insert(2, '../recognition')
from parsing_bml import *
th1_to_th0 = queue.Queue()#queue between 1 and 0 thread
th0_to_th3_1 = queue.Queue()#queue between 0 and 3 thread
th0_to_th3_2 = queue.Queue()#queue between 0 and 3 thread

def m1():
    Chbh.th1(th1_to_th0)

def s1():
    Timer.th0(th1_to_th0,th0_to_th3,th0_to_th3_2)

mastert = threading.Thread(target=m1)
th1t.start()
slavert = threading.Thread(target=s1)
th0t.start()
