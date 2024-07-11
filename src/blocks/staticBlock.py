import os

from src.blocks.block import Block
from src.visuals.staticSprite import StaticSprite

class StaticBlock(Block, StaticSprite):

    def __init__(self, x, y, borders, specs = None, path = None):

        path = path if path is not None else os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\nosprite.png')
        specs = specs if specs is not None else (50,50,1,255)

        Block.__init__(self,borders)
        StaticSprite.__init__(self,specs,path)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
