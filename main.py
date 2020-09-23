from config import *
from wall import *
from player import *
import json

pg.display.set_caption("Shooting Game")
icon = pg.image.load('gfx/target.png')
pg.display.set_icon(icon)
pg.mouse.set_visible(False)

#create objects
walls = []
levelname = 'levels/level1.json'
with open(levelname,'r',encoding='utf-8',newline='') as f:
    levelData = json.load(f)
    for attribute in levelData:
        if "Walls" in attribute:
            #load wall data
            for wall in attribute['Walls']:
                walls.append(Wall((tuple(wall['FirstPosition']),tuple(wall['SecondPosition']))))
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