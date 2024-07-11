import os

from src.blocks.staticBlock import StaticBlock

class Grass(StaticBlock):

    def __init__(self, x, y,borders):

        path = os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\blocks\\grass.png')
        specs = (50,50,1,0)

        super().__init__(x,y,borders,specs,path)

