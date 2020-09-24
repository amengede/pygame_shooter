from editorConfig import *
from mapGrid import *

class mapEditor:
    def __init__(self,program):
        self._program = program
        self._map_grid = MapGrid(125,25,850,550,self)
        self._borders = (pg.Rect(0,0,1000,24),pg.Rect(0,24,124,552),
                        pg.Rect(0,576,1000,24),pg.Rect(976,24,24,552))

    def handleMouse(self):
        pass
        
    def mouseUp(self):
        pass

    def getProgram(self):
        return self._program
        
    def draw(self):
        self._map_grid.draw()
        for b in self._borders:
            pg.draw.rect(SCREEN,DARK_BLUE_GREY,b)