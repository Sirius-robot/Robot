from queue import Queue
import queue, pygame, win32api, win32gui, win32con, game, time
from threading import Thread
from pygame.locals import *
from feature11 import Face
from DataBase import *
def putinqu():
    print("Enter")
    events = [["../images/background.png", "../images/pupil.png", "../images/eye_socket.png", "../images/eyebrows_anger.png", "../images/mouths/mouth_anger.png"],
              ["../images/background.png", "../images/pupil.png", "../images/eye_socket.png", "../images/eyebrows.png", "../images/mouths/mouth_boredom.png"],
              ["../images/background.png", "../images/pupil.png", "../images/eye_socket.png", "../images/eyebrows_embarrassment.png", "../images/mouths/mouth_embarrassment.png"]]
    events_pupils = [[80,200,300],[200,20,30],[80,200,300]]
    print("Start")
    while waitEvent:
        print("poping in queue")
        if len(events):
            ev_put = events.pop(0)
            que.put(ev_put, block=False)

        if len(events_pupils):
            ev_put_pup = events_pupils.pop(0)
            que_pup.put(ev_put_pup, block=False)
            time.sleep(1)