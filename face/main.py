import pygame
from pygame import Color

from game import Game
from text_object import TextObject
from game_object import GameObject
from eyebrows import Eyebrow
from eyes import Eye

s = Game(800, 480, 'background.jpg', 60)

while not s.game_over:
    s.run()