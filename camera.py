import pygame as pg

from src.visuals.background import Background

from src.blocks.block import Block
from src.entities.player import Player
from src.entities.enemy import Enemy

from src.blocks.finishLine import FinishLine

class CameraGroup(pg.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        self.offset = pg.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def isOnCamera(self, r):

        return pg.Rect(self.display_surface.get_rect().topleft + self.offset, self.display_surface.get_size()).colliderect(r)

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
        sprites += [i for i in self.sprites() if (isinstance(i, Block))]
        sprites += [i for i in self.sprites() if (isinstance(i, Enemy))]
        sprites += [i for i in self.sprites() if (isinstance(i, Player))]

        for sprite in sprites:
            sprite.draw(self.display_surface, self.offset)

    def update(self, gravidade):

        player = [i for i in self.sprites() if (isinstance(i, Player))][0]
        blocks = [i for i in self.sprites() if (isinstance(i, Block))]
        enemys = [i for i in self.sprites() if (isinstance(i, Enemy))]

        player.inputs()

        if not (player.died):
        
            for b in blocks:

                d = player.checkCollision(b.rect, b.borders)
                
                if not (isinstance(b,FinishLine)):

                    match d:
                        case 0:
                            player.vely = 0
                            player.rect.bottom = b.rect.top - gravidade
                            player.jumping = False
                        case 3:
                            player.vely = 0
                            player.rect.top = b.rect.bottom - gravidade
                        case 1:
                            player.velx = 0
                            player.rect.right = b.rect.left
                        case 2:
                            player.velx = 0
                            player.rect.left = b.rect.right

                else:

                    if (d > 0):
                        player.finished = True

            for e in enemys:

                t = player.checkCollision(e.enemyRect, [0,1,2,3])
                v = player.checkCollision(e.attackRect, [0,1,2,3])
                
                match t:

                    case -1:
                        pass

                    case 0:
                        player.vely = -40
                        e.kill()

                    case _:
                        player.die()

                match v:

                    case -1:
                        pass
                    case _:
                        player.die()

        player.vely += gravidade

        for i in self.sprites():
            i.update()
