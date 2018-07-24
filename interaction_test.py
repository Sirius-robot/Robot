import sys
import queue
import time
import win32api, win32process, win32con
import multiprocessing
sys.path.insert(0, 'Dynamixel')
import choose_behavior_test
import robotimer
sys.path.insert(0, 'face/programm')
import thread_event_handling
sys.path.insert(1, 'Alisnky')
from DataBase import *
sys.path.insert(2, 'recognition')
from parsing_bml import *
from th_recognitionwithbutton import *

def m1(chbh_to_timer, eventio, bh_end, q, eventi):
    choose_behavior_test.choose_behavior(chbh_to_timer, eventio, bh_end, q, eventi)

def input_func(q, eventio):
    while True:
        filename = input("Write bml name: ")
        q.put(filename)
        eventio.clear()
        eventio.wait()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    waitEvent = multiprocessing.Event()
    waitEvent.set()

    eventface = multiprocessing.Event()

    chbh_to_timer = multiprocessing.Queue()  # queue between 1 and 0 thread
    timer_to_images = multiprocessing.Queue()  # queue between 0 and 3 thread
    timer_to_eyepos = multiprocessing.Queue()  # queue between 0 and 3 thread
    bh_end = multiprocessing.Queue()  # queue between 0 and 3 thread
    q = multiprocessing.Queue()
    inact = multiprocessing.Queue()
    time1 = time.time()

    eventio = multiprocessing.Event()
    eventi = multiprocessing.Event()
    event = multiprocessing.Event()

    pygame_thread_mypygame = multiprocessing.Process(target=thread_event_handling.main_pygame, args=(timer_to_images, timer_to_eyepos, waitEvent, eventface))
    pygame_thread_mypygame.start()

    th0t = multiprocessing.Process(target=m1, args=(chbh_to_timer, eventio, bh_end, q, eventi))
    th0t.start()

    robotimer.roberttimer(chbh_to_timer, timer_to_images, timer_to_eyepos, eventio, bh_end)

    input_func(q, eventio)
