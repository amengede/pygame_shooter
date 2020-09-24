from gui_boxes import *

class OpenFileDown(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._graphic = pg.image.load('../gfx/down.png')
        self._graphic_rect = pg.Rect(self._x+12,self._y+12,32,32)

    def mouseUp(self):
        if self.mouseInside():
            self._parent.changeFileEntryRange(-1)
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        SCREEN.blit(self._graphic,self._graphic_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)