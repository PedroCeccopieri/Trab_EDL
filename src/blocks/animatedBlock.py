import os

from src.blocks.block import Block
from src.visuals.animatedSprite import AnimatedSprite

class AnimatedBlock(Block, AnimatedSprite):

    def __init__(self, x, y, borders, specs = None, states = None, paths = None):

        paths = paths if paths is not None else os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\nosprite.png')
        states = states if states is not None else ["animation"]
        specs = specs if specs is not None else (50,50,1,255)

        Block.__init__(self,borders)
        AnimatedSprite.__init__(self,specs,states,paths)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
