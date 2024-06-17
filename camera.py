import pygame as pg

from floor import Floor
from background import Background
from player import Player

class CameraGroup(pg.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        self.offset = pg.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def isOnCamera(self, r):

        return pg.Rect(self.display_surface.get_rect().topleft + self.offset, (500, 500)).colliderect(r)

    def center_target_camera(self,target):
        if not (target.rect.centerx - self.half_w < 0):
            self.offset.x = target.rect.centerx - self.half_w
        else:
            self.offset.x = 0

        self.offset.y = 0

    def draw(self, player):

        self.center_target_camera(player)

        sprites = []

        sprites += [i for i in self.sprites() if (isinstance(i, Background))]
        sprites += [i for i in self.sprites() if (isinstance(i, Floor))]
        sprites += [i for i in self.sprites() if (isinstance(i, Player))]

        # sprites += list(filter(lambda x: isinstance(x, Background), self.sprites()))
        # sprites += list(filter(lambda x: isinstance(x, Floor), self.sprites()))
        # sprites += list(filter(lambda x: isinstance(x, Player), self.sprites()))

        for sprite in sprites:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def update(self, gravidade):

        player = [i for i in self.sprites() if (isinstance(i, Player))][0]
        floors = [i for i in self.sprites() if (isinstance(i, Floor))]

        player.inputs()

        for f in floors:

            d = player.checkCollision(f.rect)

            if (d >= 0):
                if (d == 0):
                    player.vely = 0
                    player.rect.bottom = f.rect.top - gravidade
                    player.jumping = False
                elif (d == 3):
                    player.vely = 0
                    player.rect.top = f.rect.bottom - gravidade
                elif (d == 1):
                    player.velx = 0
                    player.rect.right = f.rect.left
                elif (d == 2):
                    player.velx = 0
                    player.rect.left = f.rect.right

        player.vely += gravidade

        for i in self.sprites():
            i.update()
