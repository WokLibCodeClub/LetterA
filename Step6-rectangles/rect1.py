# Set size of window
WIDTH = 640
HEIGHT = 480

# Set starting position for orange rectangle with variables ax and ay
ax = WIDTH/2
ay = HEIGHT/2

# Use variable speed to set speed for game
speed = 2

# Make variable abox to define Rectangle object.
# The four parameters in the brackets are:
#   the x coordinate of the left edge of the rectangle,
#   the y coordinate of the top edge of the rectangle,
#   the width of the rectangle in pixels
#   the height of the rectangle in pixels
abox = Rect(1, 1, 40, 30)

# Function update takes input from keyboard and updates
# variables ax, ay
def update():
    global ax, ay, WIDTH, HEIGHT
    
    # The arrow keys are used for the orange rectangle
    if keyboard.right and ax < WIDTH:
        ax = ax + speed
    if keyboard.left and ax > 0:
        ax = ax - speed
    if keyboard.down and ay < HEIGHT:
        ay = ay + speed
    if keyboard.up and ay > 0:
        ay = ay - speed
    
     # Set the new values of ax and ay to be the centre of the abox Rectangle
    abox.center = (ax, ay)

# Function draw clears the screen and draws the rectangles
def draw():
    screen.clear()
    screen.draw.rect(abox, color='orange')

