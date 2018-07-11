import pygame
from pygame import Color

from game import Game
from text_object import TextObject
from game_object import GameObject
from eyebrows import Eyebrow
from eyes import Eye


pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
background_image = pygame.image.load('..\images\background.jpg')

while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)

    br = Eyebrow(100,100,20,50, Color(255,0,0))
    br.draw(background_image)

    eye = Eye(200, 200, 50, Color(255,0,0), 5)
    eye.draw(background_image)