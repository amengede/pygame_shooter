from config import *
from wall import *
from player import *
import json

pg.display.set_caption("Shooting Game")
icon = pg.image.load('./gfx/target.png')
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
"""
#test: export the same data
levelData = []
#export walls
levelData.append({"Walls":[]})
for w in walls:
    pos = w.getPositions()
    levelData[0]["Walls"].append({"FirstPosition":pos[0],"SecondPosition":pos[1]})
exportData = json.dumps(levelData,indent=4)
with open('levels/level2.json','w',encoding='utf-8',newline='') as f:
    f.write(exportData)
    """
player = Player((200,200))

keys  = {pg.K_w:1,pg.K_a:2,pg.K_s:4,pg.K_d:8}

#main loop
running = True
key = 0
while running:
    #event handling
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key in keys:
                key += keys[event.key]
        if event.type == pg.KEYUP:
            if event.key in keys:
                key -= keys[event.key]
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