import pygame as pg
import os

class Background(pg.sprite.Sprite):

    def __init__(self, dim, block):
        super().__init__()

        path = os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\background.png')

        self.image = pg.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.w/2 + dim[0] * block, dim[1] - (self.rect.h / 2))

    def draw(self, surface, offset):

        offset_pos = self.rect.topleft - offset
        surface.blit(self.image, offset_pos)