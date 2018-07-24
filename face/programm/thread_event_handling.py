import pygame, win32api, win32gui, win32con
from pygame.locals import *
from face import Face
import os

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

def main_pygame(que, que_pup, waitEvent, eventface):
    global bg, pupil, mask, eyebrows, mouth
    pygame.init()
    surface = set_monitors()

    mask = pygame.image.load("face/images/eye_socket.png")
    bg = pygame.image.load("face/images/background.png")
    pupil = pygame.image.load("face/images/pupil.png")
    eyebrows = pygame.image.load("face/images/brows.png")
    mouth = pygame.image.load("face/images/rot.png")

    face_norm = Face(surface, bg, pupil, mask, eyebrows, mouth)
    face = face_norm

    clock = pygame.time.Clock()
    FPS = 25

    target_x = 0
    target_y = 0
    speed_x = 0
    speed_y = 0
    dif_speed_x = 0
    dif_speed_y = 0

    while waitEvent.is_set():                #get events from queue and push them into pygame_queue
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if eventface.is_set():
                        eventface.clear()
                    else:
                        eventface.set()
        if not que.empty():
            ev_get = que.get()
            if len(ev_get):
                if len(ev_get[0]):
                    path = 'face/images/'+ev_get[0]+'.png'
                    if os.path.isfile(path):
                        face.eyebrows.image = pygame.image.load(path)
                if len(ev_get[1]):
                    path = 'face/images/'+ev_get[1]+'.png'
                    if os.path.isfile(path):
                        face.mouth.image = pygame.image.load(path)
                #if ev_get[2] != 100:
                #    face.l_pupil.scale(ev_get[2], pupil)
                #    face.r_pupil.scale(ev_get[2], pupil)
            else:
                normal_face(face.eyebrows, face.mouth, face.l_pupil, face.r_pupil)

        if not que_pup.empty():                                              
            ev_get_pup = que_pup.get()   #[10000, 50, 50]
            time, target_x, target_y = ev_get_pup[2], ev_get_pup[0], -ev_get_pup[1]

            if time < 20:
                time = 20

            speed_x = (target_x - (face.l_pupil.bounds.x - face.l_pupil.init_bounds.x)) / (
                    time * FPS / 1000)
            if speed_x > target_x:
                speed_x = speed_x - target_x


            speed_y = (target_y - (face.l_pupil.bounds.y - face.l_pupil.init_bounds.y)) / (
                    time * FPS / 1000)
            if speed_y > target_y:
                speed_y = speed_y - target_y

            dif_speed_x = 0
            dif_speed_y = 0
        if speed_x > 0:
            if ((face.l_pupil.bounds.x - face.l_pupil.init_bounds.x) >= target_x):
                speed_x = 0

        elif speed_x < 0:
            if ((face.l_pupil.bounds.x - face.l_pupil.init_bounds.x) <= target_x):
                speed_x = 0

        if speed_y > 0:
            if ((face.l_pupil.bounds.y - face.l_pupil.init_bounds.y) >= target_y):
                speed_y = 0

        elif speed_y < 0:
            if ((face.l_pupil.bounds.y - face.l_pupil.init_bounds.y) <= target_y):
                speed_y = 0

        dif_speed_x += speed_x
        dif_speed_y += speed_y
        face.l_pupil.move(int(dif_speed_x), int(dif_speed_y))
        face.r_pupil.move(int(dif_speed_x), int(dif_speed_y))
        dif_speed_x -= int(dif_speed_x)
        dif_speed_y -= int(dif_speed_y)
        face.update()
        clock.tick(FPS)

    pygame.quit()

def normal_face(eyebrows, mouth, l_pupil, r_pupil):
    eyebrows.image = pygame.image.load("face/images/brows.png")
    mouth.image  = pygame.image.load("face/images/rot.png")
    l_pupil.image = pygame.image.load("face/images/pupil.png")
    r_pupil.image = pygame.image.load("face/images/pupil.png")
    l_pupil.bounds = l_pupil.init_bounds
    r_pupil.bounds = r_pupil.init_bounds


