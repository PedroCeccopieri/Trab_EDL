import os

from src.blocks.staticBlock import StaticBlock

class Dirt(StaticBlock):

    def __init__(self, x, y,borders):

        path = os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\blocks\\dirt.png')
        specs = (50,50,1,0)

        super().__init__(x,y,borders,specs,path)

