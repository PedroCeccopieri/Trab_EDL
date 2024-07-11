from src.entities.player import Player
from camera import CameraGroup
from spawners import checkBullets

from src.utils.utils import *

import pygame as pg
pg.init()

dim = widht, hight = 500, 500

clock = pg.time.Clock()
screen = pg.display.set_mode(dim)

camera = CameraGroup()

player = Player(50, 50)

from levels.l1 import *

running = True
while running:

    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    camera.empty()
    camera.add(player)

    checkBullets(blockGroup,enemyGroup)

    for b in blockGroup:
        if (camera.isOnCamera(b.rect)):
            camera.add(b)

    for b in backgroundGroup:
        if (camera.isOnCamera(b.rect)):
            camera.add(b)

    for e in enemyGroup:
        if (camera.isOnCamera(e.enemyRect)):
            camera.add(e)

    camera.update(gravidade)

    if (player.finished):
        camera.draw(finishLine)
        player.velx = 5
        if (player.rect.x > finishLine.rect.x + 500):
            player.endgame = True
    else:
        camera.draw(player)

    pg.display.flip()
    clock.tick(30)

    if (player.endgame):
        running = False

pg.quit()