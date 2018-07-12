import pygame
from pygame import Color

from game import Game
from text_object import TextObject
from game_object import GameObject
from eyebrows import Eyebrow
from eyes import Eye

s = Game(800, 600, 'background.jpg', 60)

br = Eyebrow(150,150,-20,-50, Color(255,0,0))
br.draw(s.background_image)

eye = Eye(200, 200, 50, Color(255,0,0), 5)
eye.draw(s.background_image)

while not s.game_over:
    s.run()