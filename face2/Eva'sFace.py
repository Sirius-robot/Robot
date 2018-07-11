#Hi
import pygame
import win32gui, win32api,win32con

monitors = win32api.EnumDisplayMonitors()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Call this function so the Pygame library can initialize itself
pygame.init()

screen = pygame.display.set_mode([800, 480],pygame.NOFRAME)

hmdn = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hmdn, win32con.SHOW_FULLSCREEN)
print(pygame.display.Info())
win32gui.MoveWindow(hmdn, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1],800,480,0)

clock = pygame.time.Clock()

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background = pygame.image.load("background.png").convert()
background_image = pygame.image.load("eye_socket.png").convert()

pupil = pygame.image.load("pupil.png").convert()
pupil2 = pygame.image.load("pupil.png").convert()
pupil_anger = pygame.image.load("pupil_anger.png").convert()
eyebrows = pygame.image.load("eyebrows.png").convert()
eyebrows2 = pygame.image.load("eyebrows.png").convert()
eyebrows_anger = pygame.image.load("eyebrows_anger.png").convert()
eyebrows_embarrassment = pygame.image.load("eyebrows_embarrassment.png").convert()
mouth = pygame.image.load("mouth.png").convert()
mouth2 = pygame.image.load("mouth.png").convert()
mouth_anger = pygame.image.load("mouth_anger.png").convert()

background.set_colorkey(BLACK)

pupil.set_colorkey(WHITE)
pupil2.set_colorkey(WHITE)
pupil_anger.set_colorkey(WHITE)
eyebrows.set_colorkey(WHITE)
eyebrows2.set_colorkey(WHITE)
eyebrows_anger.set_colorkey(WHITE)
eyebrows_embarrassment.set_colorkey(WHITE)
mouth.set_colorkey(WHITE)
mouth2.set_colorkey(WHITE)
mouth_anger.set_colorkey(WHITE)


done = False

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_q:
                eyebrows = pygame.transform.rotate(eyebrows2,0)
            if  event.key == pygame.K_w:
                eyebrows = pygame.transform.rotate(eyebrows_anger,0)
            if  event.key == pygame.K_e:
                eyebrows = pygame.transform.rotate(eyebrows_embarrassment,0)
            if  event.key == pygame.K_a:
                pupil = pygame.transform.rotate(pupil2,0)
            if  event.key == pygame.K_s:
                pupil = pygame.transform.rotate(pupil_anger,0)
            if  event.key == pygame.K_z:
                mouth = pygame.transform.rotate(mouth2,0)
            if  event.key == pygame.K_x:
                mouth = pygame.transform.rotate(mouth_anger,0)

    screen.blit(background_image, background_position)

    screen.blit(background, [0, 0])

    screen.blit(eyebrows, [0, 0])

    screen.blit(pupil, [0, 0])

    screen.blit(mouth, [0, 0])




    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()