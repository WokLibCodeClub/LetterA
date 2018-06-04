Changing the appearance of the letter
-------------------------------------

Before getting on to moving the letter around the screen here are some ways you can change its appearance.

To change the colour you can add this to the code:


```
def draw():
    screen.draw.text('A', center=(WIDTH/2, HEIGHT/2), color='red')
```

Again, we have to use the American spelling "color" not the British "colour". Most of the common colours can be produced just by putting the name of the colour inside quotes. But you can make your own colour by combining different amounts of the primary colours red, green and blue. To do this replace 'red' with a set of brackets, with three numbers up to 255, separated by commas, where the three numbers are the strengths of red, green and blue. So (0, 0, 255) would produce a blue colour, but (255, 255, 0) would produce yellow. (128, 0, 0) would produce a dark red colour, and (60, 0, 0) would produce a very dark red colour.

Here is code for a dark purple coloured letter A.

```
def draw():
    screen.draw.text('A', center=(WIDTH/2, HEIGHT/2), color=(128, 0, 128))
```

To change the size of the letter add a fontsize parameter. Without any fontsize parameter the size will be 24. This code will make a bigger letter A:

```
def draw():
    screen.draw.text('A', center=(WIDTH/2, HEIGHT/2), color=(128, 0, 128), fontsize=60)
```

Using variables for coordinates
-------------------------------

To make the letter move around the screen we need to change its coordinates. These are the values in part of the screen.draw.text statement in the brackets next to center=

The easiest way to have coordinates which can be changed is to use variables for the x and y coordinates. You can give these any name, but here we will call them x and y. 

To make variables you need to have statements like x = 0, or y = 100 in the part of the code below the WIDTH and HEIGHT statements. These statements will both create the variables, and give them initial values. Because the values are numbers, Python understands that these new variables will be numerical variables.

This code will create new variables and give them initial values which represent the centre of the window:

x = WIDTH/2
y = HEIGHT/2

These statements need to be placed under the WIDTH and HEIGHT statements.

In the draw function we need to change the coordinates in center= so that for the x coordinate it will use the variable x, and for the y coordinate it will use the variable y.

Make these changes and check if the letter displays properly.

Moving the letter
-----------------

we've already said that Pygame Zero looks for a function called draw in the code, but at the same time it also looks for a function called update. If it finds one it executes update first, then draw, and keeps repeating this sequence update, draw, update, draw 60 times a second. 

This means that if we make changes to the x and y coordinates in the update function, Pygame Zero will immediately afterwards draw the letter with the new coordinates. 



