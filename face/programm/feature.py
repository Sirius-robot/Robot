import pygame
from pygame.rect import Rect
class Feature:
    def __init__(self, x, y, w, h, image):
        self.back_poz = [0,0]
        self.bounds = Rect(x, y, w, h)
        self.image = pygame.image.load(image)


    def draw(self, surface):
        surface.blit(self.image, self.bounds)

    def move(self, dx, dy, speed= None):
        self.bounds = self.bounds.move(dx, dy)

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



class Eyebrows(Feature):
    def __init__(self, x, y, w, h, eyebr_image, special_effect=None):
        self.leftbrow = Feature()

        #GameObject.__init__(self, x, y,w,h, eyebr_image)
        #self.eyebr_image = pygame.image.load(eyebr_image)
        ##self.image = load(file)
        #self.special_effect = special_effect
    def move(self):
        leftbrow.move

    def draw(self, surface):
        #pygame.draw.rect(surface, self.color, self.bounds)
        surface.blit(self.eyebr_image, (100, 100))

class Eye(Feature):
    def __init__(self, x, y, r, color, speed=(0,0)):
        GameObject.__init__(self,
                            x - r,
                            y - r,
                            r * 2,
                            r * 2,
                            speed)
        self.radius = r
        self.diameter = r * 2
#      self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface,
                           self.color,
                           self.center,
                           self.radius)