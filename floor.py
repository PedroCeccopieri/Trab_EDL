import pygame as pg
import random as rd

class Floor(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pg.Surface((50, 50))
        self.image.fill((0,255,0))
        # self.image = pg.image.load("floor.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)