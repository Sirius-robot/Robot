from queue import Queue
import queue, pygame, win32api, win32gui, win32con, game, time
from threading import Thread
from pygame.locals import *
from feature11 import Feature
from feature11 import Face

waitEvent = True
que = Queue()

# Load and set up graphics.
bg = pygame.image.load("../images/background.png")
mask = pygame.image.load("../images/eye_socket.png")
pupil_norm = pygame.image.load("../images/pupil.png")
eyebrows_norm = pygame.image.load("../images/eyebrows.png")
eyebrows2 = pygame.image.load("../images/eyebrows.png")
eyebrows_anger = pygame.image.load("../images/eyebrows_anger.png")
eyebrows_embarrassment = pygame.image.load("../images/eyebrows_embarrassment.png")
eyebrows_surprise = pygame.image.load("../images/eyebrows/eyebrows_surprise.png")
mouth_norm = pygame.image.load("../images/mouths/mouth.png")
mouth2 = pygame.image.load("../images/mouths/mouth.png")
mouth_anger = pygame.image.load("../images/mouths/mouth_anger.png")
mouth_embarrassment = pygame.image.load("../images/mouths/mouth_embarrassment.png")
mouth_boredom = pygame.image.load("../images/mouths/mouth_boredom.png")
mouth_surprise = pygame.image.load("../images/mouths/mouth_surprise.png")

events = [[pygame.display.set_mode((800, 480), NOFRAME, 32), bg, pupil_norm, mask, eyebrows_anger, mouth_anger],
          [pygame.display.set_mode((800, 480), NOFRAME, 32), bg, pupil_norm, mask, eyebrows_surprise, mouth_boredom]]

def putinqu():
    while waitEvent and len(events):
        # pygame.event.post(ev_put)
        ev_put = events.pop(0)
        que.put(ev_put, block=False)
        time.sleep(1)

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

def main_pygame():
    global bg, pupil, mask, eyebrows, mouth
    background_cl = (255,255,255)
    pygame.init()
    surface = set_monitors()

    pupil = pupil_norm
    eyebrows = eyebrows_norm
    mouth = mouth_norm

    face_norm = Face(surface, bg, pupil, mask, eyebrows, mouth)
    face = face_norm

    clock = pygame.time.Clock()
    FPS = 60

    peiq = Thread(target=putinqu)  #create 3 thread, putting events in queue
    peiq.start()

    mainLoop = True
    while mainLoop:   #get events from queue and push them into pygame_queue
        try:
            ev_get = que.get()

        except queue.Empty:
            break

        else:
            #pygame.display.set_mode((800, 480), NOFRAME, 32), bg, pupil_norm, mask, eyebrows_anger, mouth_anger
            print('ok')

            surface = ev_get[0]
            bg = ev_get[1]
            pupil = ev_get[2]
            mask = ev_get[3]
            eyebrows = ev_get[4]
            mouth =  ev_get[5]
        surface.fill(background_cl)
        pygame.display.update()

        clock.tick(FPS)

        face = Face(surface, bg, pupil, mask, eyebrows, mouth)
        face.update()

    global waitEvent
    waitEvent = False
    pygame.quit()
    peiq.join()


#......
pygame_thread = Thread(target=main_pygame)
pygame_thread.start()
pygame_thread.join()
#......