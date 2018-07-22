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

    def scale(self, percents, image):

        self.image = image
        self.image = pygame.transform.scale(self.image, (int(self.init_bounds.w * 0.01 * percents),
                                                               int(self.init_bounds.h * 0.01 * percents)))

        pygame.time.wait(1000)
        #self.bounds.x += self.bounds.w * (self.percents2 - percents) / 100 / 2
        #self.bounds.y += self.bounds.h * (self.percents2 - percents) / 100 / 2
        self.percents2 = percents
