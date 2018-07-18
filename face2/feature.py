import pygame
from pygame.rect import Rect
class Feature:
    def __init__(self, x, y, w, h, image):
        self.init_x = x
        self.init_y = y
        self.i_x = 0
        self.i_y = 0
        self.init_bounds = Rect(x, y, w, h)
        self.bounds = Rect(x, y, w, h)
        self.image = image

    def draw(self, surface):
        surface.blit(self.image, self.bounds)

    def move(self, x, y, time, face):
        steps = 50 * time * 0.01
        st = int(steps)
        x = x - self.i_x
        y = y - self.i_y
        x_step = int(x / st)
        y_step = int(y / st)
        time_step = int(time / st)
        for i in range(st):
            self.bounds.x = self.bounds.x + x_step
            pygame.display.update(self.bounds)
            self.bounds.y = self.bounds.y + -y_step
            pygame.display.update(self.bounds)
            pygame.time.wait(time_step)
            print(self.bounds.x, self.bounds.y,time_step)
            face.update()
        self.i_x = x
        self.i_y = y

    def scale(self, percents):
        self.image = pygame.transform.scale(self.image, (int(self.init_bounds.w * 0.01 * percents), int(self.init_bounds.h * 0.01 * percents)))
        self.bounds.x = self.bounds.x + (self.init_bounds.w - (self.init_bounds.w * 0.01 * percents))/2
        self.bounds.y = self.bounds.y + (self.init_bounds.w - (self.init_bounds.w * 0.01 * percents))/2


'''
    def update(surface,bg , pupil, mask, eyebrows, mouth):
        self.bg.draw(self.surface)
        self.l_pupil.draw(self.surface)
        # self.mask.draw(self.surface)
        self.mouth.draw(self.surface)
        self.eyebrows.draw(self.surface)
        pygame.display.update()
'''

class Face:
    def __init__(self,surface, imgbg,imgpupil,imgmask,imgeyebrows,imgmouth,
                 l_pupil_pos = (120,135),r_pupil_pos = (520,135),mouth_pos = (0,0),eyebrows_pos = (0,0)):
        self.bg = Feature(0,0,imgbg.get_width(),imgbg.get_height(),imgbg)
        self.surface = surface
        self.mask = Feature(0,0,imgmask.get_width(),imgmask.get_height(),imgmask)
        self.l_pupil = Feature(l_pupil_pos[0],l_pupil_pos[1],imgpupil.get_width(),imgpupil.get_height(),imgpupil)
        self.r_pupil = Feature(r_pupil_pos[0],r_pupil_pos[1],imgpupil.get_width(),imgpupil.get_height(),imgpupil)
        self.mouth = Feature(mouth_pos[0],mouth_pos[1],imgmouth.get_width(),imgmouth.get_height(),imgmouth)
        self.eyebrows = Feature(eyebrows_pos[0],eyebrows_pos[1],imgeyebrows.get_width(),imgeyebrows.get_height(),imgeyebrows)


    def update(self):
        self.bg.draw(self.surface)
        self.l_pupil.draw(self.surface)
        self.r_pupil.draw(self.surface)
        #self.mask.draw(self.surface)
        self.mouth.draw(self.surface)
        self.eyebrows.draw(self.surface)
        pygame.display.update()
