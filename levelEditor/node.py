from editorConfig import *

class Node:
    def __init__(self,position):
        self._position = position
        self._renderTarget = None
    
    def getPosition(self):
        return self._position
    
    def setRenderTarget(self,target):
        self._renderTarget = target
    
    def draw(self):
        if self._renderTarget != None:
            pg.draw.circle(self._renderTarget,WHITE,self._position,4)