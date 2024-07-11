import pygame as pg
import os

from src.entities.enemy import Enemy
from src.visuals.animatedSprite import AnimatedSprite

class Frog(Enemy, AnimatedSprite):

    def __init__(self, x, y, t):

        self.towards = t
        self.attacking = False
        self.jumpping = False
        self.idle = True

        specs = (100,50,1,0)
        states = ["idle","attack","jump"]
        paths = [
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\enemies\\frog\\idle.png'),
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\enemies\\frog\\attack.png'),
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\enemies\\frog\\jump.png')]

        AnimatedSprite.__init__(self, specs, states, paths)

        rect = self.image.get_rect()
        rect.topleft = (x,y)

        self.enemyRect = pg.Rect([rect.x, rect.y, rect.w/2, rect.h])
        self.attackRect = pg.Rect([rect.x + rect.w/2, rect.y, 0, rect.h])

        if not (self.towards):
            self.flipSprites()
    
    def update(self):
    
        self.setState()
        self.animate()

    def draw(self, surface, offset):

        if not (self.towards):
            offset_pos = self.enemyRect.topleft - offset + [-self.image.get_rect().w/2,0]
        else:
            offset_pos = self.enemyRect.topleft - offset

        surface.blit(self.image, offset_pos)

    def setState(self):

        if (self.idle and pg.time.get_ticks() - self.lastStateUpdate >= 5000):
            self.idle = False
            self.attacking = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.image = self.sprites["attack"]["sprites"][self.animation]
        
        elif (self.attacking and pg.time.get_ticks() - self.lastStateUpdate >= 2000):

            self.attacking = False
            self.jumpping = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.image = self.sprites["jump"]["sprites"][self.animation]
        
        elif (self.jumpping and pg.time.get_ticks() - self.lastStateUpdate >= 2000):

            self.jumpping = False
            self.idle = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.turnAround()

            self.image = self.sprites["idle"]["sprites"][self.animation]

    def animate(self):

        if (self.idle):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

                self.animation += 1
                self.animation %= self.sprites["idle"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["idle"]["sprites"][self.animation]

        elif (self.attacking):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 80):

                self.animation += 1
                self.animation %= self.sprites["attack"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["attack"]["sprites"][self.animation]

                self.updateAttack(self.animation)

        elif (self.jumpping):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

                self.animation += 1
                self.animation %= self.sprites["jump"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["jump"]["sprites"][self.animation]

        else:
            self.image = self.sprites["idle"]["sprites"][0]

    def updateAttack(self, n):

        match n:
            case 4:
                self.attackRect.w = 2 * (self.enemyRect.w) / self.sprites["attack"]["frames"]
            case 5:
                self.attackRect.w = 5 * (self.enemyRect.w) / self.sprites["attack"]["frames"]
            case 6:
                self.attackRect.w = (self.enemyRect.w)
            case 7:
                self.attackRect.w = (self.enemyRect.w) / self.sprites["attack"]["frames"]
            case _:
                self.attackRect.w = 0

        if not (self.towards):
            self.attackRect.topright = self.enemyRect.topleft
        else:
            self.attackRect.topleft = self.enemyRect.topright

