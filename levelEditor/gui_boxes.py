from editorConfig import *
from openDialogue import *

editorImported()

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


class NewBox(Box):

    def mouseUp(self):
        if self.mouseInside():
            print("New Level")
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT.render("New Level",True,self._text_colour)
        SCREEN.blit(text,pg.Rect(self._x+40,self._y+40,self._width,self._height))
        pg.draw.rect(SCREEN,BLACK,self._box,1)

class OpenBox(Box):

    def mouseUp(self):
        if self.mouseInside():
            program = self._parent.getProgram()
            program.setActiveElement(OpenDialogue(program,self._parent))
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT.render("Open Level",True,self._text_colour)
        SCREEN.blit(text,pg.Rect(self._x+40,self._y+40,self._width,self._height))
        pg.draw.rect(SCREEN,BLACK,self._box,1)

class Container(Box):
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        pg.draw.rect(SCREEN,BLACK,self._box,1)