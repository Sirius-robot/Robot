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
        #self.br = Eyebrow(100, 100, 20, 50, Color(255, 0, 0))
        #self.br.draw(self.background_image)
#
        #self.eye = Eye(200, 200, 50, Color(255, 0, 0), 5)
        #self.eye.draw(self.background_image)


        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        #pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)#{'KEYDOWN': []}
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

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
                print('dhxfcfbd')
                if event.key == pygame.K_LEFT:
                    print('hello')
                # for handler in self.keydown_handlers[event.key]:
                #     handler(event.key)
                if event.key == pygame.K_RIGHT:
                    print('huktftiyfiy')


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
            self.surface.blit(self.background_image, (0, 0))
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(self.frame_rate)