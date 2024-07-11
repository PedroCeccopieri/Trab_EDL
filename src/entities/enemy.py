import pygame as pg

class Enemy():
    
    def update(self):
    
        self.setState()
        self.animate()

    def draw(self, surface, offset):

        offset_pos = self.enemyRect.topleft - offset
        surface.blit(self.image, offset_pos)

    def turnAround(self):
        self.flipSprites()
        self.towards = not self.towards