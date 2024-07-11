import pygame as pg
import os

from src.entities.enemy import Enemy
from src.visuals.animatedSprite import AnimatedSprite

class Bullet(Enemy, AnimatedSprite):

    def __init__(self, x, y, t):

        self.towards = t

        specs = (32,32,1,0)
        states = ["fly"]
        paths = [
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\enemies\\bullet\\fly.png')]

        AnimatedSprite.__init__(self, specs, states, paths)

        rect = self.image.get_rect()
        rect.topleft = (x,y)

        self.enemyRect = pg.Rect(rect.x, rect.y, 49, 50)
        self.attackRect = rect

        if (self.towards):
            self.velx = 5
        else:
            self.flipSprites()
            self.image = self.sprites["fly"]["sprites"][0]
            self.velx = -5
    
    def update(self):

        self.animate()

        self.enemyRect.move_ip(self.velx, 0)

        if (self.enemyRect.x < -50):
            self.kill()

    def draw(self, surface, offset):
    
        offset_pos = self.enemyRect.topleft - offset

        surface.blit(self.image, offset_pos)

    def animate(self):

        if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

            self.animation += 1
            self.animation %= self.sprites["fly"]["frames"]
            self.lastFrameUpdate = pg.time.get_ticks()

            self.image = self.sprites["fly"]["sprites"][self.animation]
