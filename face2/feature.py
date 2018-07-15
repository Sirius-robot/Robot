import pygame
from pygame.rect import Rect
class Feature:
    def __init__(self, x, y, w, h, image):
        self.init_x = x
        self.init_y = y
        self.init_bounds = Rect(x, y, w, h)
        self.bounds = Rect(x, y, w, h)
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.bounds)

    def move(self, x, y, speed= None):
        self.bounds = self.bounds.move(x, y)

    def rotate(self,  degree, speed= None):
        self.bounds = pygame.transform.rotate(self.bounds, degree)

    def change(self, x, y, w, h, image):
        self.bounds = Rect(x, y, w, h)
        self.image = pygame.image.load(image)


    def changes(self, speed):
        pass

    def update(self):
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)

class Face:
    def __init__(self,surface, imgbg,imgpupil,imgmask,imgeyebrows,imgmouth,
                 pupil_pos = (50,50),mouth_pos = (0,0),eyebrows_pos = (0,0)):
        self.bg = Feature(0,0,imgbg.get_width(),imgbg.get_height(),imgbg)
        self.surface = surface
        self.mask = Feature(0,0,imgmask.get_width(),imgmask.get_height(),imgmask)
        self.l_pupil = Feature(pupil_pos[0],pupil_pos[1],imgpupil.get_width(),imgpupil.get_height(),imgpupil)
        self.mouth = Feature(mouth_pos[0],mouth_pos[1],imgmouth.get_width(),imgmouth.get_height(),imgmouth)
        self.eyebrows = Feature(eyebrows_pos[0],eyebrows_pos[1],imgeyebrows.get_width(),imgeyebrows.get_height(),imgeyebrows)


    def update(self):
        self.bg.draw(self.surface)
        self.l_pupil.draw(self.surface)
        #self.mask.draw(self.surface)
        self.mouth.draw(self.surface)
        self.eyebrows.draw(self.surface)
        pygame.display.update()
