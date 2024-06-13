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

        self.velx = 0
        self.vely = 0

        self.jumping = False

    def inputs(self):

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.setVelx(-5)
        if keys[pg.K_RIGHT]:
            self.setVelx(5)
        if keys[pg.K_UP]:
            if not (self.jumping):
                self.setVely(-50)
                self.jumping = True

    def checkCollision(self, r):

        if (self.rect.colliderect(r)):
            self.jumping = False
            return True

        return False

    def getRect(self):

        return self.rect

    def setVelx(self, dx):

        self.velx = dx

    def setVely(self, dy):

        self.vely = dy

    def getVelx(self):
        
        return self.velx

    def getVely(self):

        return self.vely

    def addVelx(self, dx):

        self.velx += dx

    def addVely(self, dy):

        self.vely += dy

    def setX(self, nx):

        self.rect.x = nx

    def setY(self, ny):

        self.rect.y = ny

    def getX(self):

        return self.rect.x
    
    def getY(self):

        return self.rect.y

    def moveX(self, dx):

        self.rect.x += dx

    def moveY(self, dy):

        self.rect.y += dy

    def update(self):
    
        self.inputs()

        if (self.getVelx() != 0):
            self.addVelx(self.getVelx()/abs(self.getVelx()) * -1 * 0.2)

        if (self.rect.x + self.velx < 0):
            self.rect.x = 0
            self.velx = 0

        self.rect.move_ip(self.velx, self.vely)

        if (abs(self.velx) < 1):
            self.velx = 0