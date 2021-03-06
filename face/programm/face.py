import pygame
from feature import Feature

class Face:
    def __init__(self,surface, imgbg,imgpupil,imgmask,imgeyebrows,imgmouth,
                 l_pupil_pos = (127,135),r_pupil_pos = (557,135),mouth_pos = (0,0),eyebrows_pos = (0,0)):
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
        self.mask.draw(self.surface)
        self.mouth.draw(self.surface)
        self.eyebrows.draw(self.surface)
        pygame.display.update()

    def update_pupils(self):
        self.l_pupil.draw(self.surface)
        self.r_pupil.draw(self.surface)
        pygame.display.update()
