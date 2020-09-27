import pygame as pg

pg.init()

SCREEN_SIZE = (640,480)
SCREEN  = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("My Game")

running = True

while running:
    for event in pg.event.get():
        print(event)
        if event.type == pg.KEYDOWN:
            print(event)
        if event.type == pg.QUIT:
            running = False
    #draw
    #(r,g,b)
    SCREEN.fill((255,0,0))
    #line(surface, color, start_pos, end_pos, width)
    pg.draw.line(SCREEN,(0,255,0),(-100,0),(100,200),2)
    pg.display.update()