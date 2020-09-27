from editorConfig import *
from mapGrid import *
from node import *

class mapEditor:
    def __init__(self,program):
        self._program = program
        self._map_grid = MapGrid(125,25,850,550,self)
        self._mapSpace = self._map_grid.getMapSpace()
        #set render target for all game objects
        for n in program._nodes:
            program._nodes[n].setRenderTarget(self._mapSpace)
        for w in program._walls:
            w.setRenderTarget(self._mapSpace)

    def handleMouse(self):
        pass
        
    def mouseUp(self):
        pass

    def getProgram(self):
        return self._program
        
    def draw(self):
        #render game objects
        for w in self._program._walls:
            w.draw()
        for n in self._program._nodes:
            self._program._nodes[n].draw()
        self._map_grid.draw()