from collections import defaultdict
import pygame, sys
from pygame.locals import *
import game
from eyebrows import *
from feature import *
from face.images import *
import win32api, win32gui
monitors = win32api.EnumDisplayMonitors()
print(win32api.GetMonitorInfo(monitors[0][0]))
print(win32api.GetMonitorInfo(monitors[1][0])['Monitor'])



pygame.init()
surface = pygame.display.set_mode((720,480),0,32)
(x, y, w, h) = (10,40,300,200)
bgColor = (0,255,0)

pygame.init()
surface = pygame.display.set_mode((720,480),0,32)
win32gui.MoveWindow(surface, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][2],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][3],0)
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

        #elif event.type == pygame.KEYUP:
        #    for handler in keyup_handlers[event.key]:
        #        handler(event.key)
    surface.fill(bgColor)
    for i in objects:
        i.draw(surface)

    pygame.display.update()
pygame.quit()