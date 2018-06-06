# Set the size of the window by making numerical variables WIDTH and HEIGHT
WIDTH = 640
HEIGHT = 480

# Make numerical variables x and y and give them initial values.
x = WIDTH/2
y = HEIGHT/2

# Make a numerical variable to control the speed of the game
speed = 2

# Define function update where the x coordinate will be changed
def update():
    global x
    # Use if statement to check if the right arrow is being pressed and
    # if the x coordinate is less than the right edge of the window.
    # Change the x coordinate by 1 if both conditions are true.
    # If only one or neither is true then don't change the x coordinate.
    if keyboard.right and x < WIDTH:
        x = x + speed

# Define function draw which will draw the letter on the screen
def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color=(128, 0, 128), fontsize=60)
