import pygame as pg

class Floor:

    def __init__(self, screen, dim):

        self.screen = screen
        self.dim = dim
        self.w = self.dim[0]
        self.h = 50
        self.y = self.dim[1] - self.h

    def checkColision(self, hitbox):

        return hitbox[1] + hitbox[3] >= self.y

    def draw(self):

        pg.draw.rect(self.screen, (0,255,0), (0, self.y, self.w, self.h))