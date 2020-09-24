from gui_boxes import *

class ExitBox(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._graphic = pg.image.load('../gfx/close.png')
        self._graphic_rect = pg.Rect(self._x,self._y,32,32)

    def mouseUp(self):
        if self.mouseInside():
            program = self._parent.getProgram()
            program.setActiveElement(self._parent.getParent())
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        SCREEN.blit(self._graphic,self._graphic_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)