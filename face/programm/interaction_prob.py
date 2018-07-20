import threading
import sys
import time
import queue
import thread_event_handling
from threading import Thread, Event

sys.path.insert(0, 'Dynamixel')

import choose_behavior
import Timer
import servocontrol

sys.path.insert(1, 'Alisnky')

from DataBase import *

sys.path.insert(2, 'recognition')

from parsing_bml import *

waitEvent = Event()
waitEvent.set()     #waitEvent.isSet() return True

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

pygame_thread_mypygame = Thread(target=thread_event_handling.main_pygame, args=(timer_to_images, timer_to_eyepos, waitEvent))
pygame_thread_mypygame.daemon = True
pygame_thread_mypygame.start()

#pygame_thread_putinqu = Thread(target=thread_putinqu.putinqu, args=(que, que_pup, waitEvent))
#pygame_thread_putinqu.daemon = True
#pygame_thread_putinqu.start()
