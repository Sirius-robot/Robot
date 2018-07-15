from queue import Queue
import queue, pygame, win32api, win32gui, win32con, game, time
from threading import Thread
from pygame.locals import *

waitEvent = True
que = Queue()

def putinqu():
    while waitEvent:
        # pygame.event.post(myev)
        myev = pygame.event.Event(pygame.USEREVENT)
        que.put(myev, block=False)
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
    background_cl = (255,255,255)
    pygame.init()
    surface = set_monitors()

    clock = pygame.time.Clock()
    FPS = 60

    peiq = Thread(target=putinqu)  #create 3 thread, putting events in queue
    peiq.start()

    mainLoop = True
    while mainLoop:   #get events from queue and push them into pygame_queue
        try:
            ev = que.get()

        except queue.Empty:
            break

        else:
            pygame.event.post(ev)
            print('ok')
        surface.fill(background_cl)
        pygame.display.update()

        clock.tick(FPS)

    global waitEvent
    waitEvent = False
    pygame.quit()
    peiq.join()


#......
pygame_thread = Thread(target=main_pygame)
pygame_thread.start()
pygame_thread.join()
#......