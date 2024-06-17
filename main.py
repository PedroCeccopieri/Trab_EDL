from player import Player
from floor import Floor
from camera import CameraGroup

from utils import *

from level1 import *

import pygame as pg
pg.init()

dim = widht, hight = 500, 500

clock = pg.time.Clock()
screen = pg.display.set_mode(dim)


camera = CameraGroup()

player = Player(50, 50)

running = True
while running:

    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    camera.empty()
    camera.add(player)

    for s in floorGroup:
        if (camera.isOnCamera(s.rect)):
            camera.add(s)

    for b in backgroundGroup:
        if (camera.isOnCamera(b.rect)):
            camera.add(b)

    camera.update(gravidade)
    camera.draw(player)

    pg.display.flip()
    clock.tick(30)

pg.quit()