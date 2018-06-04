# Set the size of the window by making numerical variables WIDTH and HEIGHT
WIDTH = 640
HEIGHT = 480

# Make numerical variables x and y and give them initial values.
x = WIDTH/2
y = HEIGHT/2


# Define function update where the x coordinate will be changed
def update():
    global x
    # Use if statement to check if the right arrow is being pressed and
    # change the x coordinate by 1 if it is being pressed.
    # If it's not being pressed then don't change the x coordinate.
    if keyboard.right:
        x = x + 2

# Define function draw which will draw the letter on the screen
def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color=(128, 0, 128), fontsize=60)
