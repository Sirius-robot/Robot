import pygame, win32api, win32gui, win32con, game
from pygame.locals import *
from eyebrows import *
from feature import *
from face.images import *
monitors = win32api.EnumDisplayMonitors() #list of monitors' coords information/

pygame.init()
surface = pygame.display.set_mode((800,480),NOFRAME,32) #window's create

hwnd = win32gui.GetForegroundWindow()    #get id of the top window(hwnd is integer)

win32gui.ShowWindow(hwnd, win32con.SHOW_FULLSCREEN)   #fullscreen

win32gui.MoveWindow(hwnd, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],    #move this window
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1],
                    800,
                    480,0)
(x, y, w, h) = (10,40,300,200)
(x1, y1, w1, h1) = (50,100,300,200)
bgColor = (0,255,0)

eyebr = Feature(x, y, w, h, '..\images\eyebrow.png')
eyebr.draw(surface)
sm = Feature(x1, y1, w1, h1, '..\images\eyebrow.png')
sm.draw(surface)

objects = [eyebr, sm]

mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                eyebr.move(-10, 0)

            if event.key == pygame.K_RIGHT:
                eyebr.move(10, 0)

            if event.key == pygame.K_UP:
                eyebr.move(0, -10)

            if event.key == pygame.K_DOWN:
                eyebr.move(0, 10)

            if event.key == pygame.K_1:
                sm.change(300, 300,100,100,'..\images\eyebrow.png' )

    surface.fill(bgColor)
    for i in objects:
        i.draw(surface)

    pygame.display.update()
pygame.quit()