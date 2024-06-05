from player import Player
from floor import Floor

import pygame as pg
pg.init()

dim = widht, hight = 500, 500

clock = pg.time.Clock()
screen = pg.display.set_mode(dim)

player = Player(screen,10,10)
floor = Floor(screen,dim)

gravidade = 5

running = True
while running:

    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.setVely(-40)

    if pg.key.get_pressed()[pg.K_LEFT]:
        player.setVelx(-5)
    if pg.key.get_pressed()[pg.K_RIGHT]:
        player.setVelx(5)

    player.update()

    if (floor.checkColision(player.getHitBox())):
        player.setVely(0)
    else:
        player.addVely(gravidade)

    if (player.getVelx() != 0):
        player.addVelx(player.getVelx()/abs(player.getVelx()) * -1 * 0.2)

    floor.draw()
    player.draw()

    pg.display.flip()
    clock.tick(60)

pg.quit()