from config import *
import math

class Player:
    def __init__(self,position):
        self._position = pg.math.Vector2(position)
        self._direction = 0
        self._sprite = pg.image.load('gfx/right-arrow.png')
        self._speed = 1
        self._keyToDirectionMap = {1:0,2:90,3:45,4:180,6:135,7:90,8:270,9:315,11:0,12:225,13:270,14:180}
    
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
        #movement
        if keyInput in self._keyToDirectionMap:
            directionModifier = self._keyToDirectionMap[keyInput]
            self._position += pg.math.Vector2(math.cos((self._direction + directionModifier)*math.pi/180),
                                            -math.sin((self._direction + directionModifier)*math.pi/180))
    
    def draw(self):
        SCREEN.blit(self._sprite_image,self._position)