import pygame as pg
1
from floor import Floor
from background import Background

dim = widht, hight = 500, 500

backgroundGroup = pg.sprite.Group()
floorGroup = pg.sprite.Group()

for i in range(5):
    floorGroup.add(Floor(dim[0] * i, dim[1]-50, dim[0], 50))
    backgroundGroup.add(Background(dim, i))

floorGroup.add(Floor(100,300,100,50))