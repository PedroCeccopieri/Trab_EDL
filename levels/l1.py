import pygame as pg

from src.blocks.dirt import Dirt
from src.blocks.grass import Grass
from src.blocks.bulletLauncher import BulletLauncher
from src.blocks.finishLine import FinishLine
from src.entities.frog import Frog
from src.entities.bullet import Bullet
from src.visuals.background import Background

dim = widht, hight = 500, 500

backgroundGroup = pg.sprite.Group()
blockGroup = pg.sprite.Group()
enemyGroup = pg.sprite.Group()

finishLine = FinishLine(2000,350,[0,1,2,3])
blockGroup.add(finishLine)

for i in range(5):
    backgroundGroup.add(Background(dim, i))

for i in range(5):
    for j in range(10):
        blockGroup.add(Grass(dim[0] * i + dim[0] / 10 * j, dim[1]-50, [0]))

for i in range(3):
    blockGroup.add(Dirt(250 + 50 * i,450,[1,2]))
    blockGroup.add(Dirt(250 + 50 * i,400,[1,2]))
    blockGroup.add(Grass(250 + 50 * i,350,[0,1,2]))

enemyGroup.add(Frog(150,400,False))
blockGroup.add(BulletLauncher(350,300,[0,1,2,3],False))

blockGroup.add(Dirt(600,300,[0,1,2,3]))
blockGroup.add(Dirt(650,300,[0,1,2,3]))
blockGroup.add(BulletLauncher(600,400,[0,1,2,3],False))
blockGroup.add(BulletLauncher(650,400,[0,1,2,3],True))
enemyGroup.add(Frog(650,250,False))

blockGroup.add(Dirt(1000,450,[1,2]))
blockGroup.add(Dirt(1000,400,[1,2]))
blockGroup.add(Dirt(1000,350,[1,2]))
blockGroup.add(Dirt(1000,300,[1,2]))
blockGroup.add(Grass(1000,250,[0,1,2,3]))
blockGroup.add(Dirt(1150,400,[0,1,2,3]))
blockGroup.add(BulletLauncher(1150,350,[0,1,2,3],False))
blockGroup.add(BulletLauncher(1200,400,[0,1,2,3],True))

for i in range(5):
    blockGroup.add(Dirt(1450 + 50 * i,330,[0,1,2,3]))
    blockGroup.add(Dirt(1450 + 50 * i,200,[0,1,2,3]))

blockGroup.add(Dirt(1400,330,[0,1,2]))
blockGroup.add(Dirt(1350,330,[0,1,2]))
blockGroup.add(Dirt(1350,280,[1,2]))
blockGroup.add(Dirt(1350,230,[1,2]))
blockGroup.add(Dirt(1350,200,[1,2]))

blockGroup.add(Dirt(1750,400,[1,2]))
blockGroup.add(Dirt(1750,350,[1,2]))
blockGroup.add(Dirt(1750,300,[1,2]))
blockGroup.add(Dirt(1750,250,[1,2]))
blockGroup.add(Dirt(1750,200,[0,1,2]))
blockGroup.add(Dirt(1700,200,[0,1,2,3]))

blockGroup.add(BulletLauncher(1800,280,[0,1,2,3],False))
blockGroup.add(BulletLauncher(1350,150,[0,1,2,3],True))

print("DONE")