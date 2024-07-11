import pygame as pg

from src.utils.utils import getImage

class AnimatedSprite(pg.sprite.Sprite):

    def __init__(self, specs, states, paths):
        super().__init__()

        self.loadSprites(specs, states, paths)

        self.animation = 0
        self.lastFrameUpdate = pg.time.get_ticks()
        self.lastStateUpdate = pg.time.get_ticks()

    def loadSprites(self, specs, states, paths):

        self.sprites = {}

        w, h, s, c = specs

        for state, path in zip(states, paths):

            sheet = pg.image.load(path)

            frames = sheet.get_width() // w
            stateSprites = [getImage(sheet,i,w,h,s,c) for i in range(frames)]

            self.sprites[state] = {"sprites": stateSprites, "frames": frames}

        self.image = self.sprites[states[0]]["sprites"][0]

    def flipSprites(self):

        for i in self.sprites.values():
            i["sprites"] = [pg.transform.flip(j, True, False).convert_alpha() for j in i["sprites"]]

    def update(self):

        super().update()

    def draw(self, surface, offset):

        offset_pos = self.rect.topleft - offset
        surface.blit(self.image, offset_pos)

    def setState(self):

        pass

    def animate(self):
        
        pass
