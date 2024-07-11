import pygame as pg
import os

from src.utils.utils import getImage

class StaticSprite(pg.sprite.Sprite):

    def __init__(self, specs, path):
        super().__init__()

        self.loadSprite(specs, path)

    def loadSprite(self, specs, path):

        w, h, s, c = specs

        sheet = pg.image.load(path)
        self.image = getImage(sheet,0,w,h,s,c)

    def flipSprites(self):

        self.image = pg.transform.flip(self.image, True, False).convert_alpha()

    def update(self):

        super().update()

    def draw(self, surface, offset):

        offset_pos = self.rect.topleft - offset
        surface.blit(self.image, offset_pos)
