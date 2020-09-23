from config import *
import math

class Player:
    def __init__(self,position):
        self._position = pg.math.Vector2(position)
        self._direction = 0
        self._sprite = pg.image.load('gfx/right-arrow.png')
        self._speed = 1
    
    def update(self):
        #mouse look
        rel = pg.mouse.get_rel()
        self._direction += rel[0]
        if self._direction < 0:
            self._direction += 360
        elif self._direction > 360:
            self._direction -= 360

        #transform sprite
        orig_rect = self._sprite.get_rect()
        self._sprite_image = pg.transform.rotate(self._sprite, self._direction)
        rot_rect = orig_rect.copy()
        rot_rect.center = self._sprite_image.get_rect().center
        self._sprite_image = self._sprite_image.subsurface(rot_rect).copy()
    
    def handleKeys(self,keyInput):
        directionModifier = 0
        if keyInput == 0:
            #nothing is pressed
            return
        elif keyInput == 1 or keyInput == 11:
            #w
            directionModifier = 0
        elif keyInput == 2 or keyInput == 7:
            #a
            directionModifier = 90
        elif keyInput == 3:
            #w & a
            directionModifier = 45
        elif keyInput == 4 or keyInput == 14:
            #s
            directionModifier = 180
        elif keyInput == 6:
            #a & s
            directionModifier = 135
        elif keyInput == 8 or keyInput == 13:
            #d
            directionModifier = 270
        elif keyInput == 9:
            #d & w
            directionModifier = 315
        elif keyInput == 12:
            #s & d
            directionModifier = 225
        
        #run in direction
        self._position += pg.math.Vector2(math.cos((self._direction + directionModifier)*math.pi/180),
                                            -math.sin((self._direction + directionModifier)*math.pi/180))
    
    def draw(self):
        SCREEN.blit(self._sprite_image,self._position)