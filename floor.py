import pygame as pg
import random as rd

class Floor(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        super().__init__()

        self.image = pg.Surface((w, h))
        self.image.fill((0,255,0))
        # self.image = pg.image.load("floor.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def getRect(self):

        return self.rect
    
    def getY(self):

        return self.rect.y - self.rect.h