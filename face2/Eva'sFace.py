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
background = pygame.image.load("Images/background.png")
background_image = pygame.image.load("Images/eye_socket.png")

pupil = pygame.image.load("Images/pupil.png")
eyebrows = pygame.image.load("Images/eyebrows/eyebrows.png")
eyebrows2 = pygame.image.load("Images/eyebrows/eyebrows.png")
eyebrows_anger = pygame.image.load("Images/eyebrows/eyebrows_anger.png")
eyebrows_embarrassment = pygame.image.load("Images/eyebrows/eyebrows_embarrassment.png")
eyebrows_surprise = pygame.image.load("Images/eyebrows/eyebrows_surprise.png")
mouth = pygame.image.load("Images/mouths/mouth.png")
mouth2 = pygame.image.load("Images/mouths/mouth.png")
mouth_anger = pygame.image.load("Images/mouths/mouth_anger.png")
mouth_embarrassment = pygame.image.load("Images/mouths/mouth_embarrassment.png")
mouth_boredom = pygame.image.load("Images/mouths/mouth_boredom.png")
mouth_surprise = pygame.image.load("Images/mouths/mouth_surprise.png")
'''
pupil.set_colorkey(WHITE)
eyebrows.set_colorkey(WHITE)
eyebrows2.set_colorkey(WHITE)
eyebrows_anger.set_colorkey(WHITE)
eyebrows_surprise.set_colorkey(WHITE)
eyebrows_embarrassment.set_colorkey(WHITE)
mouth.set_colorkey(WHITE)
mouth2.set_colorkey(WHITE)
mouth_anger.set_colorkey(WHITE)
mouth_embarrassment.set_colorkey(WHITE)
mouth_boredom.set_colorkey(WHITE)
mouth_surprise.set_colorkey(WHITE)
'''
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
            if  event.key == pygame.K_r:
                eyebrows = pygame.transform.rotate(eyebrows_surprise,0)
            if  event.key == pygame.K_a:
                mouth = pygame.transform.rotate(mouth2,0)
            if  event.key == pygame.K_s:
                mouth = pygame.transform.rotate(mouth_anger,0)
            if  event.key == pygame.K_d:
                mouth = pygame.transform.rotate(mouth_embarrassment,0)
            if event.key == pygame.K_f:
                    mouth = pygame.transform.rotate(mouth_boredom, 0)
            if event.key == pygame.K_g:
                        mouth = pygame.transform.rotate(mouth_surprise, 0)
            if event.key == pygame.K_z:
                        pupil = pygame.transform.scale(pupil, 0, 1.5)

    screen.blit(background, [0, 0])

    screen.blit(pupil, [0, 0])

    screen.blit(background_image, background_position)

    screen.blit(eyebrows, [0, 0])


    screen.blit(mouth, [0, 0])




    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()