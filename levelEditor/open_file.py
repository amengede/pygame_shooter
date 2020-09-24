from gui_boxes import *

class OpenFile(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._graphic = pg.image.load('../gfx/open.png')
        self._graphic_rect = pg.Rect(self._x+128,self._y+8,32,32)
        self._text_rect = pg.Rect(self._x+16,self._y+8,self._width,self._height)

    def mouseUp(self):
        if self.mouseInside():
            print("Open")
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT.render("Open",True,self._text_colour)
        SCREEN.blit(text,self._text_rect)
        SCREEN.blit(self._graphic,self._graphic_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)