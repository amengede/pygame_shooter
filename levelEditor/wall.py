from editorConfig import *

class Wall:
    def __init__(self,leftNode,rightNode):
        self._left = leftNode
        self._right = rightNode
        self._renderTarget = None
    
    def getPositions(self):
        return (self._left.getPosition,self._right.getPosition)
    
    def setRenderTarget(self,target):
        self._renderTarget = target
    
    def draw(self):
        if self._renderTarget != None:
            pg.draw.line(self._renderTarget,WHITE,self._left.getPosition(),self._right.getPosition(),2)