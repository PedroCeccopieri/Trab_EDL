import pygame as pg

class Player:

    def __init__(self, screen, x, y):

        self.screen = screen
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50

        self.velx = 0
        self.vely = 0

    def getHitBox(self):

        return (self.x, self.y, self.w, self.h)

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

    def moveX(self, dx):

        self.x += dx

    def moveY(self, dy):

        self.y += dy

    def update(self):

        self.x += self.velx
        self.y += self.vely
    
    def draw(self):

        pg.draw.rect(self.screen, (0,0,0), (self.x,self.y,50,50))