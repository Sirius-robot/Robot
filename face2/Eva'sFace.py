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
background_image = pygame.image.load("background.png").convert()
eye_image = pygame.image.load("eye.png").convert()
eye2_image = pygame.image.load("eye.png").convert()
eye3_image = pygame.image.load("eye.png").convert()
smile_image = pygame.image.load("smile.png").convert()
smile2_image = pygame.image.load("smile.png").convert()
eye_image.set_colorkey(BLACK)
eye2_image.set_colorkey(BLACK)
eye3_image.set_colorkey(BLACK)
smile_image.set_colorkey(BLACK)
smile2_image.set_colorkey(BLACK)

done = False

wink = True

while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_s:
                smile_image = pygame.transform.flip(smile_image,300,300)
            if  (event.key == pygame.K_w)and(wink == True):
                eye_image = pygame.transform.flip(smile2_image,100,100)
                eye2_image = pygame.transform.flip(smile2_image,100,100)
                wink = False
            else:
                eye_image = pygame.transform.flip(eye3_image, 100, 100)
                eye2_image = pygame.transform.flip(eye3_image, 100, 100)
                wink = True

    # Copy image to screen:
    screen.blit(background_image, background_position)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.


    # Copy image to screen:
    screen.blit(eye_image, [100, 100])
    screen.blit(eye2_image, [500, 100])
    screen.blit(smile_image, [300, 300])


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()