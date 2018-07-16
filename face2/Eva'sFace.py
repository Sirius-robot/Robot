#Hi
import pygame
import win32gui, win32api,win32con

from feature import Face, Feature

monitors = win32api.EnumDisplayMonitors()

# Call this function so the Pygame library can initialize itself
pygame.init()

surface = pygame.display.set_mode([800, 480],pygame.NOFRAME, 32)

hmdn = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hmdn, win32con.SHOW_FULLSCREEN)
print(pygame.display.Info())
win32gui.MoveWindow(hmdn, win32api.GetMonitorInfo(monitors[1][0])['Monitor'][0],
                    win32api.GetMonitorInfo(monitors[1][0])['Monitor'][1],800,480,0)

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
bg =  pygame.image.load("Images/background.png")
mask =  pygame.image.load("Images/eye_socket.png")

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



moveeye = pygame.event.Event(pygame.USEREVENT+1, time = 80, x = 200, y = 300)
moveeye1 = pygame.event.Event(pygame.USEREVENT+1, time = 200, x = 20, y = 30)
pygame.event.post(moveeye)
pygame.event.post(moveeye1)

done = False

steps = 5
face = Face(surface,bg , pupil, mask, eyebrows, mouth)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event == moveeye:
            x_step = moveeye.x // steps
            y_step = moveeye.y // steps
            time_step = moveeye.time // steps
            for i in range (1,steps+1):
                print(face.l_pupil.init_bounds.x)
                print(face.l_pupil.init_bounds.y)
                print(face.l_pupil.bounds.x)
                print(face.l_pupil.bounds.y)
                pygame.time.wait(time_step)
                face.l_pupil.move(x_step * i, y_step * i)
                face.update()
            print(face.l_pupil.init_bounds.x)
            print(face.l_pupil.init_bounds.y)
            print(face.l_pupil.bounds.x)
            print(face.l_pupil.bounds.y)
            pygame.time.wait(moveeye.time % steps)
            face.update()
        elif event == moveeye1:
            x_step = moveeye1.x // steps
            y_step = moveeye1.y // steps
            time_step = moveeye1.time // steps
            for i in range(1, steps + 1):
                print(face.l_pupil.init_bounds.x)
                print(face.l_pupil.init_bounds.y)
                print(face.l_pupil.bounds.x)
                print(face.l_pupil.bounds.y)
                pygame.time.wait(time_step)
                face.l_pupil.move(x_step * i, y_step * i)
                face.update()
            print(face.l_pupil.init_bounds.x)
            print(face.l_pupil.init_bounds.y)
            print(face.l_pupil.bounds.x)
            print(face.l_pupil.bounds.y)
            pygame.time.wait(moveeye1.time % steps)
            face.update()
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_q:
                eyebrows = pygame.transform.rotate(eyebrows2,0)
            elif  event.key == pygame.K_w:
                eyebrows = pygame.transform.rotate(eyebrows_anger,0)
            elif event.key == pygame.K_e:
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

    surface.fill((0,0,0))
    face.update()


pygame.quit()