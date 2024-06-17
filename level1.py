import pygame as pg
1
from floor import Floor
from background import Background

dim = widht, hight = 500, 500

backgroundGroup = pg.sprite.Group()
floorGroup = pg.sprite.Group()

for i in range(5):
    backgroundGroup.add(Background(dim, i))

for i in range(5):
    for j in range(10):
        floorGroup.add(Floor(dim[0] * i + dim[0] / 10 * j, dim[1]-50))


floorGroup.add(Floor(200,400))
floorGroup.add(Floor(200,350))
floorGroup.add(Floor(200,300))

print("DONE")