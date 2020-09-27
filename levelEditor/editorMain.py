from editorConfig import *
from editor import *

pg.display.set_caption("Level Editor")
icon = pg.image.load('../gfx/target.png')
pg.display.set_icon(icon)

#main loop
running = True
key = 0
program = Editor()
while running:
    #event handling
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            program.getActiveElement().mouseUp()
        if event.type == pg.QUIT:
            running = False
    program.getActiveElement().handleMouse()
    
    #object updates

    #rendering
    SCREEN.fill(DARK_BLUE_GREY)
    program.getActiveElement().draw()
    pg.display.update()
    CLOCK.tick()
    fps = CLOCK.get_fps()
    pg.display.set_caption("Running at "+str(int(fps))+" fps")

    #timing: 60fps
    #CLOCK.tick(60)