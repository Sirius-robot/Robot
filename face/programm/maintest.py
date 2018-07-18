from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
import test_thread, mypygame
from threading import Thread, Event
from pygame.locals import *
from feature11 import Face
from pygame import *

waitEvent = Event()
waitEvent.set()         #waitEvent.isSet() return True

que = Queue()
que_pup = Queue()

pygame_thread_mypygame= Thread(target=mypygame.main_pygame, args = (que, que_pup, waitEvent))
pygame_thread_mypygame.start()

pygame_thread_putinqu = Thread(target=test_thread.putinqu, args = (que, que_pup, waitEvent))
pygame_thread_putinqu.start()
print("before join")
try:
    pygame_thread_putinqu.join()
    pygame_thread_mypygame.join()
except KeyboardInterrupt:
    print("interrupt")
    waitEvent.clear()
print("after join")