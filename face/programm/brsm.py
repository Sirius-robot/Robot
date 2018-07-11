import pygame
from pygame.rect import Rect
class Brsm:
    def __init__(self, x, y, w, h, image):
        self.bounds = Rect(x, y, w, h)
        self.image = pygame.image.load(image)

    def change(self, file):
        pass
