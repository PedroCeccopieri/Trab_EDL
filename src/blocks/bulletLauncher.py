import pygame as pg
import os

from src.blocks.animatedBlock import AnimatedBlock
from src.entities.bullet import Bullet

class BulletLauncher(AnimatedBlock):

    def __init__(self, x, y,borders, t):

        self.towards = t
        self.idle = True
        self.blinking = False
        self.attacking = False
        self.shoot = False

        specs = (50,50,1,0)
        states = ["blink","attack"]
        paths = [
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\blocks\\launcher\\blink.png'),
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\blocks\\launcher\\attack.png')]
        
        super().__init__(x,y,borders,specs,states,paths)

        if not (self.towards):
            self.flipSprites()

    def update(self):

        self.setState()
        self.animate()

    def setState(self):

        if (self.idle and pg.time.get_ticks() - self.lastStateUpdate >= 3000):
            self.idle = False
            self.blinking = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.image = self.sprites["blink"]["sprites"][self.animation]
        
        elif (self.blinking and pg.time.get_ticks() - self.lastStateUpdate >= 1000):

            self.blinking = False
            self.attacking = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.image = self.sprites["attack"]["sprites"][self.animation]
        
        elif (self.attacking and pg.time.get_ticks() - self.lastStateUpdate >= 500):

            self.attacking = False
            self.idle = True
            self.lastStateUpdate = pg.time.get_ticks()

            self.animation = 0

            self.image = self.sprites["blink"]["sprites"][self.animation]
            self.shoot = True

    def animate(self):

        if (self.blinking):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 80):

                self.animation += 1
                self.animation %= self.sprites["blink"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["blink"]["sprites"][self.animation]

        elif (self.attacking):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

                self.animation += 1
                self.animation %= self.sprites["attack"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["attack"]["sprites"][self.animation]

        else:
            self.image = self.sprites["blink"]["sprites"][0]

    def getBullet(self):
        return Bullet(self.rect.x,self.rect.y,self.towards)

