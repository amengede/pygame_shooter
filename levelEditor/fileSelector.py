from editorConfig import *
from openDialogue import *
from gui_boxes import *

class fileSelector:
    def __init__(self,program):
        self._program = program
        self._new_box = NewBox(125,200,200,100,self)
        self._open_box = OpenBox(325,200,200,100,self)

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