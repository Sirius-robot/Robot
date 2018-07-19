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

