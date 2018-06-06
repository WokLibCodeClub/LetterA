# Set size of window
WIDTH = 640
HEIGHT = 480

# Use variable speed to set speed for game
speed = 4

# Make a Boolean variable to show if there is a collision
collision = False

# Make variables abox and bbox to define Rectangle objects.
# The four parameters in the brackets are:
#   the x coordinate of the left edge of the rectangle,
#   the y coordinate of the top edge of the rectangle,
#   the width of the rectangle in pixels
#   the height of the rectangle in pixels
abox = Rect(1, 1, 35, 40)
bbox = Rect(50, 50, 35, 40)

# Function startup sets the initial positions for the boxes
def startup():
    global ax, ay, bx, by
    # Set starting position for orange rectangle with variables ax and ay
    # This is 3/4 of the way to the right and 3/4 of the way to the bottom
    ax = WIDTH*3/4
    ay = HEIGHT*3/4

    # Set starting position for red rectangle with variables bx and by
    # This is 1/4 of the way to the right and 1/4 of the way to the bottom
    bx = WIDTH/4
    by = HEIGHT/4
    
    # Reset ax and ay to be the centre of the abox Rectangle
    abox.center = (ax, ay)
    # Reset bx and by to be the centre of the bbox Rectangle
    bbox.center = (bx, by)

# When we first run the programme we have to call function startup to set
# the initial positions
startup()

# Function update takes input from keyboard and updates
# variables ax, ay, bx, by
def update():
    global ax, ay, bx, by, collision
    
    # Test if the two boxes are overlapping and put result in collision
    collision = abox.colliderect(bbox)
    
    # If there is a collision stop the game and wait for key x
    if collision:
        if keyboard.x:
            # startup() resets the letter positions
            collision = False
            startup()
    # If there is no collision continue using the keys to move the letters
    else:
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
    screen.draw.textbox('A', abox, color='orange')
    screen.draw.rect(abox, color='orange')
    screen.draw.textbox('B', bbox, color='red')
    screen.draw.rect(bbox, color='red')
    
    # If there is a collision then draw 'BANG' in the middle of the window
    if collision:
            screen.draw.text('BANG!', center=(WIDTH/2, HEIGHT/2), fontsize=180, color='red')
            # Extra instruction to exit the game
            screen.draw.text('Press x to restart', (30, HEIGHT - 30))
    
