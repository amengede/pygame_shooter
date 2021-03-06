from gui_boxes import *
from openDialogue import *
class OpenBox(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._graphic = pg.image.load('../gfx/open.png').convert_alpha()
        self._graphic_rect = pg.Rect(self._x+146,self._y+96,64,64)
        self._text_rect = pg.Rect(self._x+40,self._y+40,self._width,self._height)

    def mouseUp(self):
        if self.mouseInside():
            program = self._parent.getProgram()
            program.setActiveElement(OpenDialogue(program,self._parent))
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT.render("Open Level",True,self._text_colour)
        SCREEN.blit(text,self._text_rect)
        SCREEN.blit(self._graphic,self._graphic_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)