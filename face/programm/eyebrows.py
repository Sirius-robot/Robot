import pygame
from game_object import GameObject

class Eyebrow(GameObject):
    def __init__(self, x, y, w, h, eyebr_image, special_effect=None):
        GameObject.__init__(self, x, y,w,h, eyebr_image)
        self.eyebr_image = pygame.image.load(eyebr_image)
        #self.image = load(file)
        self.special_effect = special_effect



    def draw(self, surface):
        #pygame.draw.rect(surface, self.color, self.bounds)
        surface.blit(self.eyebr_image, (100, 100))
