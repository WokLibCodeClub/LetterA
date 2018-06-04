Using variables for coordinates
-------------------------------

To make the letter move around the screen we need to change its coordinates. These are the values in part of the screen.draw.text statement in the brackets next to center=

The easiest way to have coordinates which can be changed is to use variables for the x and y coordinates. You can give these any name, but here we will call them x and y. 

To make variables you need to have statements like x = 0, or y = 100 in the part of the code below the WIDTH and HEIGHT statements. These statements will both create the variables, and give them initial values. Because the values are numbers, Python understands that these new variables will be numerical variables.

This code will create new variables and give them initial values which represent the centre of the window:

x = WIDTH/2
y = HEIGHT/2

These statements need to be placed under the WIDTH and HEIGHT statements because they use the values of WIDTH and HEIGHT in the calculation.

In the draw function we need to change the coordinates in center= so that for the x coordinate it will use the variable x, and for the y coordinate it will use the variable y.

Make these changes and check if the letter displays properly.

Moving the letter
-----------------

We've already said that Pygame Zero looks for a function called draw in the code, but at the same time it also looks for a function called update. If it finds one it executes update first, then draw, and keeps repeating this sequence update, draw, update, draw 60 times a second. 

This means that if we make changes to the x and y coordinates in the update function, Pygame Zero will immediately afterwards draw the letter with the new coordinates. This is how to make the letter move around the screen.

Create the function update above the function draw using this code
```
def update():
    x = x + 1
```
The Python code inside the function looks like mathematical nonsense, but to Python it means take the present value of the variable x, add 1 to it and put this new value back in the variable x. If you remember that x is the x coordinate of the letter in the window what effect do you think this change of variable x would have?


