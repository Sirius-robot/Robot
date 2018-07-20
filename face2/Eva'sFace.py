import pygame
import win32gui, win32api, win32con

from feature import Face, Feature

monitors = win32api.EnumDisplayMonitors()

# Call this function so the Pygame library can initialize itself
pygame.init()

surface = pygame.display.set_mode([800, 480], pygame.NOFRAME)

hmdn = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hmdn, win32con.SHOW_FULLSCREEN)
print(pygame.display.Info())
win32gui.MoveWindow(hmdn, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1], 800, 480, 0)

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
bg = pygame.image.load("Images/background.png")
mask = pygame.image.load("Images/eye_socket.png")

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

moveeye = pygame.event.Event(pygame.USEREVENT + 1, time=10000, x=-50, y=-50)
# moveeye1 = pygame.event.Event(pygame.USEREVENT+1, time = 1000, x = 20, y = -20)
pygame.event.post(moveeye)
# pygame.event.post(moveeye1)

done = False

clock = pygame.time.Clock()
FPS = 25

target_x = 0
target_y = 0
speed_x = 0
speed_y = 0

face = Face(surface, bg, pupil, mask, eyebrows, mouth)
face.update()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event == moveeye:

            target_x = moveeye.x
            target_y = -moveeye.y
            speed_x = (target_x - (face.l_pupil.bounds.x - face.l_pupil.init_bounds.x)) / (
                        moveeye.time / 2 * FPS / 1000)
            print(speed_x)
            speed_y = (target_y - (face.l_pupil.bounds.y - face.l_pupil.init_bounds.y)) / (
                        moveeye.time / 2 * FPS / 1000)
            dif_speed_x = 0
            dif_speed_y = 0
            print(face.l_pupil.bounds.x)
            print(face.l_pupil.bounds.y)

    if speed_x > 0:
        if ((face.l_pupil.bounds.x - face.l_pupil.init_bounds.x) >= target_x):
            print("Stop x")
            speed_x = 0
    elif speed_x < 0:
        if ((face.l_pupil.bounds.x - face.l_pupil.init_bounds.x) <= target_x):
            print("Stop x")
            face.l_pupil.scale(150, pupil)
            face.r_pupil.scale(150, pupil)
            face.update()
            pygame.time.wait(1000)
            face.l_pupil.scale(30, pupil)
            face.r_pupil.scale(30, pupil)
            face.update()
            pygame.time.wait(1000)
            face.l_pupil.scale(150, pupil)
            face.r_pupil.scale(150, pupil)
            face.update()
            pygame.time.wait(1000)
            speed_x = 0

    if speed_y > 0:
        if ((face.l_pupil.bounds.y - face.l_pupil.init_bounds.y) >= target_y):
            print("Stop y")
            speed_y = 0
    elif speed_y < 0:
        if ((face.l_pupil.bounds.y - face.l_pupil.init_bounds.y) <= target_y):
            print("Stop y")

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