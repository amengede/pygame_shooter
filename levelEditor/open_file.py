from gui_boxes import *
from node import *
from wall import *
from editor import *
from mapEditor import *
import json

class OpenFile(Box):
    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._graphic = pg.image.load('../gfx/open.png').convert_alpha()
        self._graphic_rect = pg.Rect(self._x+128,self._y+8,32,32)
        self._text_rect = pg.Rect(self._x+16,self._y+8,self._width,self._height)

    def mouseUp(self):
        if self.mouseInside():
            program = self._parent.getProgram()
            levelname = self._parent.getCurrentLevel()
            with open(levelname,'r',encoding='utf-8',newline='') as f:
                levelData = json.load(f)
                for attribute in levelData:
                    if "Walls" in attribute:
                        #load wall data
                        for wall in attribute['Walls']:

                            first_position = tuple(wall['FirstPosition'])
                            if first_position not in program._nodes:
                                program._nodes[first_position] = Node(first_position)

                            second_position = tuple(wall['SecondPosition'])
                            if second_position not in program._nodes:
                                program._nodes[second_position] = Node(second_position)

                            program._walls.append(Wall(program._nodes[first_position],program._nodes[second_position]))
            program.setActiveElement(mapEditor(program))
    
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        text = FONT.render("Open",True,self._text_colour)
        SCREEN.blit(text,self._text_rect)
        SCREEN.blit(self._graphic,self._graphic_rect)
        pg.draw.rect(SCREEN,BLACK,self._box,1)