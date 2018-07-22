import threading
from threading import Event, Thread
import sys
import queue
sys.path.insert(0, 'Dynamixel')
import choose_behavior
import Timer
sys.path.insert(0, 'face/programm')
import thread_event_handling
sys.path.insert(1, 'Alisnky')
from DataBase import *
sys.path.insert(2, 'recognition')
from parsing_bml import *

waitEvent = Event()
waitEvent.set()

chbh_to_timer = queue.Queue()#queue between 1 and 0 thread
timer_to_images = queue.Queue()#queue between 0 and 3 thread
timer_to_eyepos = queue.Queue()#queue between 0 and 3 thread
bh_end = queue.Queue()#queue between 0 and 3 thread
q = queue.Queue()

def m1():
    choose_behavior.choose_behavior(chbh_to_timer,eventio,bh_end,)

def s1():
    Timer.timer(chbh_to_timer,timer_to_images,timer_to_eyepos,eventio,bh_end)

pygame_thread_mypygame = Thread(target=thread_event_handling.main_pygame, args=(timer_to_images, timer_to_eyepos, waitEvent))
pygame_thread_mypygame.start()

eventio = threading.Event()
event = threading.Event()

th1t = threading.Thread(target=m1)
th1t.start()
th0t = threading.Thread(target=s1)
th0t.start()
