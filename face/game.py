import pygame, sys
from collections import defaultdict
from eyes import Eye
from eyebrows import Eyebrow
from pygame import Color

class Game:
    def __init__(self,
                 #caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):

        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False

        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        #pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)#{'KEYDOWN': []}
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

        self.br = Eyebrow(100, 100, 100, 20, Color(0,100,0))
        self.br.draw(self.background_image)

        self.br2 = Eyebrow(700, 100, -100, 20, Color(0,100,0))
        self.br2.draw(self.background_image)

        self.eye = Eye(200, 200, 50, Color(0,100,0))
        self.eye.draw(self.background_image)

        self.eye2 = Eye(600,200, 50, Color(0,100,0))
        self.eye2.draw(self.background_image)

        self.objects = [self.br, self.eye, self.br2, self.eye2]
    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.br2.move(0, -10)

                if event.key == pygame.K_RIGHT:
                    self.br.move(0, 10)
                    self.br2.move(0, 10)

                if event.key == pygame.K_UP:
                    self.br.move(0, -10)
                    self.br2.move(0, -10)

                if event.key == pygame.K_DOWN:
                    self.br.move(0, 10)
                    self.br2.move(0, 10)

                if event.key == pygame.K_v:
                    self.br.pygame.transform.rotate(10)
                    #vself.br.transform.rotate(10)

            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)

            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)
    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (50, 50))
            self.handle_events()
            #self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.frame_rate)