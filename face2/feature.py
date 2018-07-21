import pygame
from pygame.rect import Rect
class Feature:
    def __init__(self, x, y, w, h, image):
        self.init_x = x
        self.init_y = y
        self.i_x = 0
        self.i_y = 0
        self.p = 0
        self.init_bounds = Rect(x, y, w, h)
        self.bounds = Rect(x, y, w, h)
        self.image = image
        self.percents2 = 100

    def draw(self, surface):
        surface.blit(self.image, self.bounds)

    def move(self, x, y, speed = None):
        self.bounds = self.bounds.move(x, y)

    def scale(self, percents, image, face):

        self.image = image
        self.image = pygame.transform.smoothscale(self.image, (int(self.init_bounds.w * 0.01 * percents), int(self.init_bounds.h * 0.01 * percents)))

        pygame.time.wait(1000)
        # self.bounds.x = (self.init_bounds.w - (self.bounds.w ))/2 + self.bounds.x
        # self.bounds.y = (self.init_bounds.h - (self.bounds.h ))/2 + self.bounds.y
        print("W =", self.init_bounds.w)
        print("H =", self.init_bounds.h)
        self.bounds.x += self.bounds.w * (self.percents2 - percents)/ 100 / 2
        self.bounds.y += self.bounds.h * (self.percents2 - percents) / 100 / 2
        self.percents2 = percents



class Face:
    def __init__(self,surface, imgbg,imgpupil,imgmask,imgeyebrows,imgmouth,
                 l_pupil_pos = (120,135),r_pupil_pos = (545,135),mouth_pos = (0,0),eyebrows_pos = (0,0)):
        self.bg = Feature(0,0,imgbg.get_width(),imgbg.get_height(),imgbg)
        self.surface = surface
        self.mask = Feature(0,0,imgmask.get_width(),imgmask.get_height(),imgmask)
        self.l_pupil = Feature(l_pupil_pos[0],l_pupil_pos[1],imgpupil.get_width(),imgpupil.get_height(),imgpupil)
        self.r_pupil = Feature(r_pupil_pos[0],r_pupil_pos[1],imgpupil.get_width(),imgpupil.get_height(),imgpupil)
        self.mouth = Feature(mouth_pos[0],mouth_pos[1],imgmouth.get_width(),imgmouth.get_height(),imgmouth)
        self.eyebrows = Feature(eyebrows_pos[0],eyebrows_pos[1],imgeyebrows.get_width(),imgeyebrows.get_height(),imgeyebrows)


    def update(self):
        self.bg.draw(self.surface)
        self.l_pupil.draw(self.surface)
        self.r_pupil.draw(self.surface)
        #self.mask.draw(self.surface)
        self.mouth.draw(self.surface)
        self.eyebrows.draw(self.surface)
        pygame.display.update()

    def update_pupils(self):
        self.l_pupil.draw(self.surface)
        self.r_pupil.draw(self.surface)
        pygame.display.update()
