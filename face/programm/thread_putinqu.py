from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
from threading import Thread
from pygame.locals import *
def  putinqu(que, que_pup, waitEvent):
    events = [["../images/eyebrows_anger.png", "../images/mouths/mouth_anger.png", 100],
              ["../images/eyebrows.png", "../images/mouths/mouth_boredom.png", 100],
              ["../images/eyebrows_embarrassment.png", "../images/mouths/mouth_embarrassment.png", 100],
              ["", "../images/mouths/mouth_anger.png", 100],
              []]
              #["", "../images/mouths/mouth_embarrassment.png", 100]]
    events_pupils = [[50,50, 400],[20, -50, 40],[-50,30, 40]]
    print("Start")
    while waitEvent:
        #print("poping in queue")
        if len(events):
            ev_put = events.pop(0)
            que.put(ev_put, block=False)

        if len(events_pupils):
            ev_put_pup = events_pupils.pop(0)
            que_pup.put(ev_put_pup, block=False)
        time.sleep(5)