Changing the appearance of the letter
-------------------------------------

Before getting on to controlling the movement of the letter around the screen here are some ways you can change its appearance.

To change the colour you can add this to the code:


```
def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color='red')
```

Again, we have to use the American spelling "color" not the British "colour". Most of the common colours can be produced just by putting the name of the colour inside quotes. But you can make your own colour by combining different amounts of the primary colours red, green and blue. To do this replace 'red' with a set of brackets, with three numbers up to 255, separated by commas, where the three numbers are the strengths of red, green and blue. So (0, 0, 255) would produce a blue colour, but (255, 255, 0) would produce yellow. (128, 0, 0) would produce a dark red colour, and (60, 0, 0) would produce a very dark red colour.

Here is code for a dark purple coloured letter A.

```
def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color=(128, 0, 128))
```

To change the size of the letter add a fontsize parameter. Without any fontsize parameter the size will be 24. This code will make a bigger letter A:

```
def draw():
    screen.clear()
    screen.draw.text('A', center=(x, y), color=(128, 0, 128), fontsize=60)
```

Changing the text that is drawn
-------------------------------

You don't need to use a letter A for this code. You can put any text inside the quotes and it will be drawn on the screen. But you can also use a text variable here.

If you make a text variable (do this in the top part of the programme where the other variables are being created), for example with:
```
c = 'cabbage'
```
then change the draw function to:

```
def draw():
    screen.clear()
    screen.draw.text(c, center=(x, y), color=(128, 0, 128), fontsize=60)
```
it will draw the word cabbage on the screen instead of letter A.

One advantage of using a text variable instead of text in quotes here is that with a variable you can get the text which is drawn to change as the code runs. You could, for example, write your code so that instead of a word it would draw the x coordinate as the text moved around.

Controlling the movement of the letter
--------------------------------------

A very useful trick for moving things about inside a window is to have the movement controlled by the arrow keys. This section shows how to make the letter move to the right IF the right arrow is pressed but to stay still if the right arrow is not pressed.

This uses a Python statement called (not surprisingly) an **if** statement.

To make this work we first need some code which will tell us if the right arrow is being pressed, then we write some code to say what should happen when the right arrow is being pressed.

An if statement starts with the word **if**, followed by what it is you want to test, followed by a colon. Then on the next lines you write code for everything that you want to happen if what you want to test is true. VERY IMPORTANT: everything that you want to happen because of the if statement must be indented.

Here is how the update function would look with an if statement:

```
def update():
    global x
    if keyboard.right:
        x = x + 1
```

```keyboard.right``` is the Pygame Zero code to check if the right arrow is being pressed. Note, this is special Pygame Zero code, and won't work unless you run your code with pgzrun. If it is being pressed the code goes on to the next line and increases the x coordinate by 1. But if it's not being pressed the code skips this line and leaves the x coordinate unchanged. 

Note that the line with the word **if** is indented because it's inside the update function, but the line x = x + 1 is indented *TWICE* because it's inside the update function *AND* inside the if statement.

Make this change then save the code and run it with pgzrun.

Remember that Pygame Zero is repeatedly running function update, then function draw very quickly, so it will detect almost instantly when you start or stop pressing the right arrow.

The Python code [letterA2.py](letterA2.py), included with this step, shows the code to make the right arrow move the letter to the right.

Challenge
=========
Add three more if statements inside function update, all very similar to this one, so that you can use the left arrow to move the letter to the left, the up arrow to move it upwards and the down arrow to move it downwards. Remember each of the if statements needs to be indented once, but the code inside the if statements needs to be indented twice.

Challenge
=========
When you have all four if statements working you might want to change how fast the letter moves. But now you've got to change something in four different places. And if you then decide you changed it too much you would have to make another change in four different places. 

How could you add a new variable to your code to control the speed so that when you wanted to change the speed you only needed to make a change in one place?

[Go to step 4](../Step4-restrict_movement)
