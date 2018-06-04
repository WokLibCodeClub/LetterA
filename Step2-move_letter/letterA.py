# A typical game loop looks a bit like this:
# while game_has_not_ended():
#    process_input()
#    update()
#    draw()

# draw()
#    Called by Pygame Zero when it needs to redraw your game window.
#    draw() must take no arguments.

#Pygame Zero attempts to work out when the game screen needs to be redrawn to avoid redrawing if nothing has changed. On each step of the game loop it will draw the screen in the following situations:

#    If you have defined an update() function (see below).
#    If a clock event fires.
#    If an input event has been triggered.
# Don't attempt to modify or animate within the draw() function - use the update() function

# update() or update(dt)

#    Called by Pygame Zero to step your game logic. This will be called repeatedly, 60 times a second, unless
#    the function is called with parameter dt which is the update time in seconds.

WIDTH = 640
HEIGHT = 480

x = WIDTH/2
y = HEIGHT/2


def update():
    global x
    #x += 1

def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color=(128,0,128), fontsize=24)
    screen.draw.text('A', center=(x-20, y), color=(128,0,128))


