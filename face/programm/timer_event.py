import pygame
MOVE_SIDE = 1000
MOVE_DOWN = 3500
clock = pygame.time.Clock()
move_side_event = pygame.USEREVENT + 1
move_down_event = pygame.USEREVENT + 2
reloaded_event  = pygame.USEREVENT + 3
pygame.time.set_timer(move_side_event, MOVE_SIDE)
pygame.time.set_timer(move_down_event, MOVE_DOWN)