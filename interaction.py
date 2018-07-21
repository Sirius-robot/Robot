import threading
import sys
import time
import queue

sys.path.insert(0, 'Dynamixel')

import choose_behavior
import Timer
import servocontrol

sys.path.insert(1, 'Alisnky')

from DataBase import *

sys.path.insert(2, 'recognition')

from parsing_bml import *
chbh_to_timer = queue.Queue()#queue between 1 and 0 thread
timer_to_images = queue.Queue()#queue between 0 and 3 thread
timer_to_eyepos = queue.Queue()#queue between 0 and 3 thread

def m1():
    choose_behavior.choose_behavior(chbh_to_timer,event)

def s1():
    Timer.timer(chbh_to_timer,timer_to_images,timer_to_eyepos,event)
event = threading.Event()
th1t = threading.Thread(target=m1)
th1t.start()
th0t = threading.Thread(target=s1)
th0t.start()
