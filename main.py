from config import *
from wall import *
from player import *

pg.display.set_caption("Shooting Game")
icon = pg.image.load('gfx/target.png')
pg.display.set_icon(icon)
pg.mouse.set_visible(False)

#create objects
walls = [Wall(((100,100),(500,50))),
        Wall(((500,50),(550,400))),
        Wall(((550,400),(350,320))),
        Wall(((350,320),(120,380))),
        Wall(((120,380),(100,100)))]

player = Player((200,200))

keys  = {'w':1,'a':2,'s':4,'d':8}

#main loop
running = True
key = 0
while running:
    #event handling
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                key += keys['w']
            elif event.key == pg.K_a:
                key += keys['a']
            elif event.key == pg.K_s:
                key += keys['s']
            elif event.key == pg.K_d:
                key += keys['d']
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                key -= keys['w']
            elif event.key == pg.K_a:
                key -= keys['a']
            elif event.key == pg.K_s:
                key -= keys['s']
            elif event.key == pg.K_d:
                key -= keys['d']
            if event.key==pg.K_ESCAPE:
                running = False
    
    #object updates
    player.update()
    player.handleKeys(key)


    #rendering
    SCREEN.fill(BLACK)
    for wall in walls:
        wall.draw()
    player.draw()
    pg.display.update()

    #timing: 60fps
    CLOCK.tick(60)