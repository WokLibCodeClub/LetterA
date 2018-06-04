# Set the size of the window by making numerical variables WIDTH and HEIGHT
WIDTH = 640
HEIGHT = 480

# Make numerical variables x and y and give them initial values.
x = WIDTH/2
y = HEIGHT/2


# Define function update where the x coordinate will be changed
def update():
    global x
    x = x + 1

# Define function draw which will draw the letter on the screen
def draw():
    screen.draw.text('A', center=(x, y))


