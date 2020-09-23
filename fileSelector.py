from editorConfig import *
from openDialogue import *

class fileSelector:
    def __init__(self,program):
        self._program = program
        self._x = 125
        self._y = 200
        self._box_width = 200
        self._box_height = 100
        self._new_box = pg.Rect(self._x,self._y,self._box_width,self._box_height)
        self._new_box_colour = BLUE_GREY
        self._new_text_colour = LIGHT_BLUE_GREY
        self._open_box = pg.Rect(self._x+self._box_width,self._y,self._box_width,self._box_height)
        self._open_box_colour = BLUE_GREY
        self._open_text_colour = LIGHT_BLUE_GREY
    
    def mouseInNew(self):
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] >= self._x and mouse_pos[0] <= (self._x + self._box_width) and\
            mouse_pos[1] >= self._y and mouse_pos[1] < (self._y + self._box_height):
            return True
        return False

    def mouseInOpen(self):
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] > (self._x + self._box_width) and mouse_pos[0] <= (self._x + 2*self._box_width) and\
            mouse_pos[1] >= self._y and mouse_pos[1] <= (self._y + self._box_height):
            return True
        return False

    def handleMouse(self):
        mouse_pos = pg.mouse.get_pos()
        #check new box
        if self.mouseInNew():
            self._new_box_colour = LIGHT_BLUE_GREY
            self._new_text_colour = WHITE
        else:
            self._new_box_colour = BLUE_GREY
            self._new_text_colour = LIGHT_BLUE_GREY

        if self.mouseInOpen():
            self._open_box_colour = LIGHT_BLUE_GREY
            self._open_text_colour = WHITE
        else:
            self._open_box_colour = BLUE_GREY
            self._open_text_colour = LIGHT_BLUE_GREY
        
    def mouseUp(self):
        if self.mouseInNew():
            #open the new map dialogue
            print("New Map")
        if self.mouseInOpen():
            #open the open map dialogue
            self._program.setActiveElement(openDialogue(self._program,self))

    
    def draw(self):
        pg.draw.rect(SCREEN,self._new_box_colour,self._new_box)
        new_text = FONT.render("New Level",True,self._new_text_colour)
        SCREEN.blit(new_text, pg.Rect(self._x + 20,self._y+30,75,25))
        pg.draw.rect(SCREEN,BLACK,self._new_box,1)
        pg.draw.rect(SCREEN,self._open_box_colour,self._open_box)
        open_text = FONT.render("Open Level",True,self._open_text_colour)
        SCREEN.blit(open_text, pg.Rect(self._x + 240,self._y+30,75,25))
        pg.draw.rect(SCREEN,BLACK,self._open_box,1)