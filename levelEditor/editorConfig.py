import pygame as pg

pg.init()

SCREEN_SIZE = (1000,800)
SCREEN  = pg.display.set_mode(SCREEN_SIZE)

#Colours
BLACK = (0,0,0)
DARK_BLUE_GREY = (31,36,40)
DARK_GREEN_GREY = (31,40,36)
DARK_RED_GREY = (40,31,36)
DARK_ORANGE_GREY = (40,36,31)
BLUE_GREY = (63,73,81)
GREEN_GREY = (63,81,72)
RED_GREY = (81,63,72)
ORANGE_GREY = (81,72,63)
LIGHT_BLUE_GREY = (126,146,162)
LIGHT_GREEN_GREY = (126,162,146)
LIGHT_RED_GREY = (162,126,146)
LIGHT_ORANGE_GREY = (162,146,126)
WHITE = (255,255,255)

#Fonts
FONT = pg.font.Font('freesansbold.ttf', 24)

CLOCK = pg.time.Clock()
FRAMERATE = 60

def editorImported():
    print("Editor Configuration was imported")