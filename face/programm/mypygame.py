from queue import Queue
import queue, pygame, win32api, win32gui, win32con, time
from threading import Thread
from pygame.locals import *
from feature11 import Face
#from DataBase import *
import test_thread
#print(database.eyes('face'))

#breakall = False
#waitEvent = True
#que = Queue()
#que_pup = Queue()

#Load and set up graphics.
#bg = pygame.image.load("../images/background.png")
#mask = pygame.image.load("../images/eye_socket.png")
#pupil_norm = pygame.image.load("../images/pupil.png")
#eyebrows_norm = pygame.image.load("../images/eyebrows.png")
#eyebrows2 = pygame.image.load("../images/eyebrows.png")
#eyebrows_anger = pygame.image.load("../images/eyebrows_anger.png")
#eyebrows_embarrassment = pygame.image.load("../images/eyebrows_embarrassment.png")
#eyebrows_surprise = pygame.image.load("../images/eyebrows/eyebrows_surprise.png")
#mouth_norm = pygame.image.load("../images/mouths/mouth.png")
#mouth2 = pygame.image.load("../images/mouths/mouth.png")
#mouth_anger = pygame.image.load("../images/mouths/mouth_anger.png")
#mouth_embarrassment = pygame.image.load("../images/mouths/mouth_embarrassment.png")
#mouth_boredom = pygame.image.load("../images/mouths/mouth_boredom.png")
#mouth_surprise = pygame.image.load("../images/mouths/mouth_surprise.png")

def movepup():
    pass

def set_monitors():
    global hwnd
    surface = pygame.display.set_mode((800, 480), NOFRAME, 32)  # window's create
    monitors = win32api.EnumDisplayMonitors()  # list of monitors' coords information/

    hwnd = win32gui.GetForegroundWindow()  # get id of the top window(hwnd is integer)

    win32gui.ShowWindow(hwnd, win32con.SHOW_FULLSCREEN)  # fullscreen

    win32gui.MoveWindow(hwnd, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],  # move this window
                        win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1],
                        800,
                        480, 0)
    return surface

def main_pygame(que, que_pup, waitEvent):
    global bg, pupil, mask, eyebrows, mouth
    background_cl = (255,255,255)
    pygame.init()
    surface = set_monitors()

    mask = pygame.image.load("../images/eye_socket.png")
    bg = pygame.image.load("../images/background.png")
    pupil = pygame.image.load("../images/pupil.png")
    eyebrows = pygame.image.load("../images/eyebrows.png")
    mouth = pygame.image.load("../images/mouths/mouth.png")

    face_norm = Face(surface, bg, pupil, mask, eyebrows, mouth)
    face = face_norm

    clock = pygame.time.Clock()
    FPS = 60

    #peiq = Thread(target=test_thread.putinqu)  #create 3 thread, putting events in queue
    #peiq.start()

    while waitEvent.is_set():                #get events from queue and push them into pygame_queue
        if not que.empty():
            ev_get = que.get()
            if len(ev_get)>0:
                if len(ev_get[0])>0:
                    face.eyebrows.image = pygame.image.load(ev_get[0])
                if len(ev_get[1])>0:
                    face.mouth.image = pygame.image.load(ev_get[1])
            else:
                normal_face(face.eyebrows, face.mouth)

        if not que_pup.empty():
            ev_get_pup = que_pup.get()
            steps = 5
            #events_pupils = [[80,200,300],[200,20,30],[80,200,300]]
            x_step = ev_get_pup[1] // steps
            y_step = ev_get_pup[2] // steps
            time_step = ev_get_pup[0] // steps
            for i in range(steps):
                pygame.time.wait(time_step)
                face.pupil.move(x_step * i, y_step * i)
                face.update()
            pygame.time.wait(ev_get_pup[0] % steps)
            face.update()
        clock.tick(FPS)
        face.update()

    pygame.quit()

#def break_all(breakall):
#    breakall.set()
#    return breakall

def normal_face(eyebrows, mouth):
    eyebrows.image = pygame.image.load("../images/eyebrows.png")
    mouth.image  = pygame.image.load("../images/mouths/mouth.png")


#......
#ygame_thread = Thread(target=main_pygame)
#ygame_thread.start()
#ygame_thread.join()
#......