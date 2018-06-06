# Set size of window
WIDTH = 640
HEIGHT = 480

# Set starting position for orange rectangle with variables ax and ay
# This is 3/4 of the way to the right and 3/4 of the way to the bottom
ax = WIDTH*3/4
ay = HEIGHT*3/4

# Set starting position for red rectangle with variables bx and by
# This is 1/4 of the way to the right and 1/4 of the way to the bottom
bx = WIDTH/4
by = HEIGHT/4

# Use variable speed to set speed for game
speed = 2

# Make a Boolean variable to show if there is a collision
collision = False

# Make a text variable to contain the text to display
coll_text = 'collision = False'

# Make variables abox and bbox to define Rectangle objects.
# The four parameters in the brackets are:
#   the x coordinate of the left edge of the rectangle,
#   the y coordinate of the top edge of the rectangle,
#   the width of the rectangle in pixels
#   the height of the rectangle in pixels
abox = Rect(1, 1, 40, 30)
bbox = Rect(50, 50, 30, 40)

# Function update takes input from keyboard and updates
# variables ax, ay, bx, by
def update():
    global ax, ay, bx, by, WIDTH, HEIGHT, collision, coll_text
    
    # Test if the two boxes are overlapping and put result in collision
    collision = abox.colliderect(bbox)
    
    # Change the text variable coll_text depending if collision is True or False
    if collision:
        coll_text = 'collision = True'
    else:
        coll_text = 'collision = False'

    # The arrow keys are used for the orange rectangle
    if keyboard.right and ax < WIDTH:
        ax = ax + speed
    if keyboard.left and ax > 0:
        ax = ax - speed
    if keyboard.down and ay < HEIGHT:
        ay = ay + speed
    if keyboard.up and ay > 0:
        ay = ay - speed
    
    # Keys a, w, s, d are used for the red rectangle
    if keyboard.d and bx < WIDTH:
        bx = bx + speed
    if keyboard.a and bx > 0:
        bx = bx - speed
    if keyboard.s and by < HEIGHT:
        by = by + speed
    if keyboard.w and by > 0:
        by = by - speed
    
     # Set the new values of ax and ay to be the centre of the abox Rectangle
    abox.center = (ax, ay)
     # Set the new values of bx and by to be the centre of the bbox Rectangle
    bbox.center = (bx, by)

# Function draw clears the screen and draws the rectangles 
# and the text showing the value of collision
def draw():
    screen.clear()
    screen.draw.rect(abox, color='orange')
    screen.draw.rect(bbox, color='red')
    screen.draw.text(coll_text, center=(WIDTH/2, HEIGHT-30))

