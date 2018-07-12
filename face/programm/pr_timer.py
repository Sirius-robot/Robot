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

# Load and set up graphics.
background = pygame.image.load("../images/background.png")
background_image = pygame.image.load("../images/eye_socket.png")

pupil = pygame.image.load("../images/pupil.png")
eyebrows = pygame.image.load("../images/eyebrows.png")
eyebrows2 = pygame.image.load("../images/eyebrows.png")
eyebrows_anger = pygame.image.load("../images/eyebrows_anger.png")
eyebrows_embarrassment = pygame.image.load("../images/eyebrows_embarrassment.png")
eyebrows_surprise = pygame.image.load("../images/eyebrows_surprise.png")
mouth = pygame.image.load("../images/mouth.png")
mouth2 = pygame.image.load("../images/mouth.png")
mouth_anger = pygame.image.load("../images/mouth_anger.png")
mouth_embarrassment = pygame.image.load("../images/mouth_embarrassment.png")
mouth_boredom = pygame.image.load("../images/mouth_boredom.png")
mouth_surprise = pygame.image.load("../images/mouth_surprise.png")


eyebr = Feature(x, y, w, h, '../images/eyebrow.png')
eyebr.draw(surface)
sm = Feature(x1, y1, w1, h1, '../images/eyebrow.png')
sm.draw(surface)

objects = [background, pupil, background_image, eyebrows, mouth, eyebr, sm]

#MOVE_SIDE = 1000
#MOVE_DOWN = 3500
#clock = pygame.time.Clock()
#move_side_event = pygame.USEREVENT + 1
#move_down_event = pygame.USEREVENT + 2
#reloaded_event  = pygame.USEREVENT + 3
#pygame.time.set_timer(move_side_event, MOVE_SIDE)
#pygame.time.set_timer(move_down_event, MOVE_DOWN)



mainLoop = True
#pygame.time.set_timer(eyebr.move(-10, 0), 10)
#pygame.time.set_timer(USEREVENT, delay)
while mainLoop:
    #clock.tick(1)
    #pygame.time.set_timer(eyebr.move(-10, 0), 10)
    for event in pygame.event.get():
        if event.type == move_side_event:
            sm.move(10, 0)
        elif event.type == move_down_event:
            sm.move(0, 10)
        elif event.type == reloaded_event:
            # when the reload timer runs out, reset it
            reloaded = True
            pygame.time.set_timer(reloaded_event, 0)

        if event.type == QUIT:
            mainLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sm.move(-10, 0)

            elif event.key == pygame.K_RIGHT:
                sm.move(10, 0)

            elif event.key == pygame.K_UP:
                sm.move(0, -10)

            elif event.key == pygame.K_DOWN:
                sm.move(0, 10)

            elif event.key == pygame.K_1:
                sm.change(300, 300,100,100,'../images/eyebrow.png' )

            elif  event.key == pygame.K_q:
                eyebrows = pygame.transform.rotate(eyebrows2,0)
            elif  event.key == pygame.K_w:
                eyebrows = pygame.transform.rotate(eyebrows_anger,0)
            elif  event.key == pygame.K_e:
                eyebrows = pygame.transform.rotate(eyebrows_embarrassment,0)
            elif  event.key == pygame.K_r:
                eyebrows = pygame.transform.rotate(eyebrows_surprise,0)
            elif  event.key == pygame.K_a:
                mouth = pygame.transform.rotate(mouth2,0)
            elif  event.key == pygame.K_s:
                mouth = pygame.transform.rotate(mouth_anger,0)
            elif  event.key == pygame.K_d:
                mouth = pygame.transform.rotate(mouth_embarrassment,0)
            elif event.key == pygame.K_f:
                mouth = pygame.transform.rotate(mouth_boredom, 0)
            elif event.key == pygame.K_g:
                mouth = pygame.transform.rotate(mouth_surprise, 0)

    surface.fill(bgColor)
    for i in objects:
        i.draw(surface)

    pygame.display.update()
pygame.quit()