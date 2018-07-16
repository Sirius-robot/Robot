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
background = Feature(0,0,800,480,"../images/background.png")
eye_socket = Feature(0,0,800,480,"../images/eye_socket.png")

pupil1 = Feature(122,137,116,117,"../images/onepupil.png")
pupil2 = Feature(562,137,116,117,"../images/onepupil.png")

eyebrows_norm = Feature(0,0,800,480,"../images/eyebrows.png")
eyebrows_anger = Feature(0,0,800,480,"../images/eyebrows_anger.png")
eyebrows_embarrassment = Feature(0,0,800,480,"../images/eyebrows_embarrassment.png")
eyebrows_surprise = Feature(0,0,800,480,"../images/eyebrows/eyebrows_surprise.png")
mouth = Feature(0,0,800,480,"../images/mouths/mouth.png")
mouth2 = Feature(0,0,800,480,"../images/mouths/mouth.png")
mouth_anger = Feature(0,0,800,480,"../images/mouths/mouth_anger.png")
mouth_embarrassment = Feature(0,0,800,480,"../images/mouths/mouth_embarrassment.png")
mouth_boredom = Feature(0,0,800,480,"../images/mouths/mouth_boredom.png")
mouth_surprise = Feature(0,0,800,480,"../images/mouths/mouth_surprise.png")


sm = Feature(x1, y1, w1, h1, '../images/eyebrows/eyebrows.png')
#sm.draw(surface)




MOVE_SIDE = 1000
MOVE_DOWN = 3500
clock = pygame.time.Clock()
move_side_event = pygame.USEREVENT + 1
move_down_event = pygame.USEREVENT + 2
reloaded_event  = pygame.USEREVENT + 3
pygame.time.set_timer(move_side_event, MOVE_SIDE)
pygame.time.set_timer(move_down_event, MOVE_DOWN)

eyebrows = eyebrows_norm
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

        elif event.type == QUIT:
            mainLoop = False

        elif event.type == pygame.KEYDOWN:
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
                eyebrows = eyebrows_anger
            elif  event.key == pygame.K_w:
                eyebrows = eyebrows_norm
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

    objects = [background, pupil1, pupil2, eye_socket, eyebrows, mouth, sm]

    for i in objects:
        i.draw(surface)

    pygame.display.update()
pygame.quit()