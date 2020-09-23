import pygame as pg

pg.init()

SCREEN_SIZE = (640,480)
SCREEN  = pg.display.set_mode(SCREEN_SIZE)

#Colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#Fonts
FONT = pg.font.Font('freesansbold.ttf', 12)

CLOCK = pg.time.Clock()
FRAMERATE = 60