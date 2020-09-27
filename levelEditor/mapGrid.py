from gui_boxes import *

class MapGrid(Box):

    def __init__(self,x,y,w,h,parent):
        super().__init__(x,y,w,h,parent)
        self._mapSpace = pg.Surface((w,h))
        self._visibleRegion = self._mapSpace.subsurface(pg.Rect(0,0,w,h))
        #fill visible region with background colour
        pg.draw.rect(self._visibleRegion,BLUE_GREY,self._visibleRegion.get_rect())
    
    def getMapSpace(self):
        return self._mapSpace

    def draw(self):
        SCREEN.blit(self._mapSpace,(self._x,self._y),self._visibleRegion.get_rect())
        pg.draw.rect(self._visibleRegion,BLUE_GREY,self._visibleRegion.get_rect())
        for x in range(self._x,self._x+self._width,25):
            pg.draw.line(SCREEN, DARK_GREEN_GREY, (x,self._y), (x,self._y+self._height), 1)
        for y in range(self._y,self._y+self._height,25):
            pg.draw.line(SCREEN, DARK_GREEN_GREY, (self._x,y), (self._x+self._width,y), 1)
        pg.draw.rect(SCREEN,BLACK,self._box,1)