import pygame as pg

from utils import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pg.Surface((50,50))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = pg.math.Vector2()
        self.speed = 1
        self.powerup = 0

        self.velx = 0
        self.vely = 0

        self.jumping = False

    def inputs(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.velx = -10
        if keys[pg.K_RIGHT]:
            self.velx = 10
        if keys[pg.K_UP]:
            if not (self.jumping):
                self.vely += -75
                self.jumping = True

    def checkCollision(self, r):

        cx = pg.Rect(self.rect.x + self.velx, self.rect.y, self.rect.w, self.rect.h).colliderect(r)
        cy = pg.Rect(self.rect.x, self.rect.y + self.vely, self.rect.w, self.rect.h).colliderect(r)
        
        if (self.velx >= 0 and cx and (self.rect.top >= r.top or self.rect.bottom <= r.bottom)):
            return 1
        elif (self.velx < 0 and cx and (self.rect.top >= r.top or self.rect.bottom <= r.bottom)):
            return 2
        elif (self.vely >= 0 and cy and self.rect.bottom <= r.top):
            return 0
        elif (self.vely < 0 and cy and self.rect.top >= r.bottom):
            return 3

        return -1

    def update(self):
    
        if (self.velx != 0):
            self.velx += self.velx / abs(self.velx) * -1 * 0.4

        if (abs(self.velx) < 1): # to stop
            self.velx = 0

        if (self.rect.x + self.velx < 0): # not to go out of bounds
            self.rect.x = 0
            self.velx = 0

        self.rect.move_ip(self.velx, self.vely)