from gui_boxes import *

class MapGrid(Box):
        
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        for x in range(self._x,self._x+self._width,25):
            pg.draw.line(SCREEN, DARK_GREEN_GREY, (x,self._y), (x,self._y+self._height), 1)
        for y in range(self._y,self._y+self._height,25):
            pg.draw.line(SCREEN, DARK_GREEN_GREY, (self._x,y), (self._x+self._width,y), 1)
        pg.draw.rect(SCREEN,BLACK,self._box,1)