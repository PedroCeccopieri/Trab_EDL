import pygame as pg
import os

from src.visuals.animatedSprite import AnimatedSprite

class Player(AnimatedSprite):

    def __init__(self, x, y):
    
        self.towards = True
        self.walking = False
        self.jumpping = False
        self.idle = True

        self.died = False
        self.finished = False
        self.endgame = False

        specs = (34,50,1,0)
        states = ["idle","walk","died"]
        paths = [
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\capybara\\idle.png'),
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\capybara\\walk.png'),
            os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\capybara\\died.png')]

        super().__init__(specs, states, paths)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.speed = 1
        self.powerup = 0

        self.velx = 0
        self.vely = 0

        self.animation = 0
        self.lastUpdate = pg.time.get_ticks()

    def inputs(self):

        if not (self.died or self.finished):

            keys = pg.key.get_pressed()

            if keys[pg.K_LEFT]:

                if (self.towards):
                    self.flipSprites()

                self.velx = -10
                self.walking = True
                self.towards = False
                self.idle = False

            elif keys[pg.K_RIGHT]:

                if not (self.towards):
                    self.flipSprites()

                self.velx = 10
                self.walking = True
                self.towards = True
                self.idle = False
                
            else:
                self.walking = False
                self.idle = True

            if keys[pg.K_UP]:
                if not (self.jumping):
                    self.vely += -50
                    self.jumping = True

    def checkCollision(self, r, borders):

        T = pg.Rect(self.rect.x + self.velx, self.rect.y + self.vely, self.rect.w, self.rect.h)

        if (T.colliderect(r)):
            top = self.rect.bottom - r.top
            rig = self.rect.right - r.left
            lef = r.right - self.rect.left
            bot = r.bottom - self.rect.top

            l = [top,rig,lef,bot]
            d = l.index(min(l))

            return d if (d in borders) else -1

        else:
            return -1

    def update(self):
    
        if not (self.died):
            if (self.velx != 0):
                self.velx += self.velx / abs(self.velx) * -1 * 0.9

            if (abs(self.velx) < 1): # to stop
                self.velx = 0

            if (self.rect.x + self.velx < 0): # not to go out of bounds
                self.rect.x = 0
                self.velx = 0

        self.animate()

        self.rect.move_ip(self.velx, self.vely)

    def animate(self):

        if (self.died):

            self.image = self.sprites["died"]["sprites"][0]

            if (pg.time.get_ticks() - self.lastFrameUpdate > 1000):
                self.endgame = True

        elif (self.idle):

            if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

                self.animation += 1
                self.animation %= self.sprites["idle"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["idle"]["sprites"][self.animation]
        
        if (self.walking):
        
            if (pg.time.get_ticks() - self.lastFrameUpdate >= 100):

                self.animation += 1
                self.animation %= self.sprites["walk"]["frames"]
                self.lastFrameUpdate = pg.time.get_ticks()

                self.image = self.sprites["walk"]["sprites"][self.animation]

    def turnAround(self):
        self.flipSprites()
        self.towards = not self.towards

    def die(self):
        self.vely = -50
        self.died = True
  