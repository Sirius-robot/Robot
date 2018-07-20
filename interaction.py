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
    choose_behavior.choose_behavior(chbh_to_timer)

def s1():
    Timer.timer(chbh_to_timer,timer_to_images,timer_to_eyepos)

chbht = threading.Thread(target=m1)
chbht.start()
timert = threading.Thread(target=s1)
timert.start()
