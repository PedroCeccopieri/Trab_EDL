import pygame as pg
import os

from src.blocks.staticBlock import StaticBlock

class FinishLine(StaticBlock):

    def __init__(self, x, y,borders):

        path = os.path.join(os.path.dirname( __file__ ), '..\\..\\sprites\\blocks\\finishline.png')
        specs = (50,100,1,0)

        super().__init__(x,y,borders,specs,path)