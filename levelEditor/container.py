from gui_boxes import *

class Container(Box):

    def setColour(self,colour):
        self._box_colour = colour
        
    def draw(self):
        pg.draw.rect(SCREEN,self._box_colour,self._box)
        pg.draw.rect(SCREEN,BLACK,self._box,1)