from editorConfig import *

class openDialogue:
    def __init__(self,program,parent):
        self._program = program
        self._parent = parent
        self._x = 100
        self._y = 80
        self._box_width = 450
        self._box_height = 350
        #container
        self._total_box = pg.Rect(self._x,self._y,self._box_width,self._box_height)
        self._total_box_colour = BLUE_GREY
        #exit
        self._exit_box = pg.Rect(self._x+self._box_width-30,self._y,30,30)
        self._exit_box_colour = RED_GREY
        #files
        self._files_x = 130
        self._files_y = 110
        self._files_width = 360
        self._files_height = 270
        self._files_box = pg.Rect(self._files_x,self._files_y,self._files_width,self._files_height)

    def mouseInExit(self):
        mouse_pos = pg.mouse.get_pos()
        if mouse_pos[0] > (self._x+self._box_width-30) and mouse_pos[0] < (self._x+self._box_width) and\
            mouse_pos[1] > self._y and mouse_pos[1] < (self._y + 30):
            return True
        return False

    def handleMouse(self):
        if self.mouseInExit():
            self._exit_box_colour = LIGHT_RED_GREY
        else:
            self._exit_box_colour = RED_GREY
        
    def mouseUp(self):
        if self.mouseInExit():
            self._program.setActiveElement(self._parent)

    
    def draw(self):
        #container
        pg.draw.rect(SCREEN,self._total_box_colour,self._total_box)
        pg.draw.rect(SCREEN,BLACK,self._total_box,1)
        #exit
        pg.draw.circle(SCREEN, self._exit_box_colour, (535,95), 15)
        pg.draw.circle(SCREEN, BLACK, (535,95), 15,1)
        #files
        pg.draw.rect(SCREEN,BLACK,self._files_box,1)