from gui_boxes import *

class Container(Box):
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        pg.draw.rect(SCREEN,BLACK,self._box,1)