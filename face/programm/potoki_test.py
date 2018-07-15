import threading, time
import Thread
from Queue import Queue
import pygame, win32api, win32gui, win32con, game
from pygame.locals import *
from eyebrows import *
from feature import *
from face.images import *

queue = Queue()
THREADS_COUNT = 2
LOCK = threading.RLock()


class MyThread(Thread):
    """
    A threading example
    """
    global MOVE_SIDE, MOVE_DOWN
    MOVE_SIDE = 1000
    MOVE_DOWN = 3500
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name


    def run(self):
        """Запуск потока"""
        while mainLoop:
            MOVE_SIDE += 20
            MOVE_DOWN += 20
            move_side_event = pygame.USEREVENT + 1
            move_down_event = pygame.USEREVENT + 2
            reloaded_event = pygame.USEREVENT + 3
            pygame.time.set_timer(move_side_event, MOVE_SIDE)
            pygame.time.set_timer(move_down_event, MOVE_DOWN)
