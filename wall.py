from config import *

class Wall:
    def __init__(self,positions):
        self._left = positions[0]
        self._right = positions[1]
    
    def draw(self):
        pg.draw.line(SCREEN,WHITE,self._left,self._right)