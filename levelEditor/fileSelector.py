from editorConfig import *
from new_box import *
from open_box import *

class fileSelector:
    def __init__(self,program):
        self._program = program
        self._new_box = NewBox(250,200,250,200,self)
        self._open_box = OpenBox(500,200,250,200,self)

    def handleMouse(self):
        self._new_box.handleMouse()
        self._open_box.handleMouse()
        
    def mouseUp(self):
        self._new_box.mouseUp()
        self._open_box.mouseUp()

    def getProgram(self):
        return self._program
        
    def draw(self):
        self._new_box.draw()
        self._open_box.draw()