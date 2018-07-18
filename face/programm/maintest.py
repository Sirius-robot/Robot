from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
from threading import Thread
from pygame.locals import *
from feature11 import Face
from DataBase import *
from test_thread import *
from pygame import *

waitEvent = True
que = Queue()
que_pup = Queue()

pygame_thread = Thread(target=pygame.main_pygame)
pygame_thread.start()
pygame_thread.join()
