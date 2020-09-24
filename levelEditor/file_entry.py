from gui_boxes import *

class FileEntry(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._text_rect = pg.Rect(self._x+8,self._y+6,self._width,self._height)
    
    def setName(self,name):
        self._text = name
    
    def getName(self):
        return self._text

    def mouseUp(self):
        if self.mouseInside():
            self._parent.setCurrentLevel(self._text)
    
    def draw(self,selected):
        if selected:
            self._box_colour = LIGHT_BLUE_GREY
        else:
            self._box_colour = BLUE_GREY
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT_SMALL.render(self._text,True,BLACK)
        SCREEN.blit(text,self._text_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)