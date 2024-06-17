import pygame as pg


class Background(pg.sprite.Sprite):

    def __init__(self, dim, block):
        super().__init__()

        self.image = pg.Surface((dim[0], dim[1]))
        self.image.fill((0,0,255))
        # self.image = pg.image.load("background.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect.w/2 + dim[0] * block, dim[1] - (self.rect.h / 2))