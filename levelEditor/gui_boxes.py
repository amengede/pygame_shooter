from editorConfig import *

class Box:
    def __init__(self,x,y,w,h,parent):
        self._parent = parent
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._box_colour = BLUE_GREY
        self._text_colour = LIGHT_BLUE_GREY
        self._box = pg.Rect(self._x,self._y,self._width,self._height)

    def mouseInside(self):
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] > self._x and mouse_pos[0] < (self._x + self._width) and\
            mouse_pos[1] > self._y and mouse_pos[1] < (self._y + self._height):
            return True
        return False
    
    def handleMouse(self):
        #check new box
        if self.mouseInside():
            self._box_colour = LIGHT_BLUE_GREY
            self._text_colour = WHITE
        else:
            self._box_colour = BLUE_GREY
            self._text_colour = LIGHT_BLUE_GREY