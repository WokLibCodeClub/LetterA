Changing the appearance of the letter
-------------------------------------

Before getting on to controlling the movement of the letter around the screen here are some ways you can change its appearance.

To change the colour you can add this to the code:


```
def draw():
    screen.draw.text('A', center=(x, y), color='red')
```

Again, we have to use the American spelling "color" not the British "colour". Most of the common colours can be produced just by putting the name of the colour inside quotes. But you can make your own colour by combining different amounts of the primary colours red, green and blue. To do this replace 'red' with a set of brackets, with three numbers up to 255, separated by commas, where the three numbers are the strengths of red, green and blue. So (0, 0, 255) would produce a blue colour, but (255, 255, 0) would produce yellow. (128, 0, 0) would produce a dark red colour, and (60, 0, 0) would produce a very dark red colour.

Here is code for a dark purple coloured letter A.

```
def draw():
    screen.draw.text('A', center=(x, y), color=(128, 0, 128))
```

To change the size of the letter add a fontsize parameter. Without any fontsize parameter the size will be 24. This code will make a bigger letter A:

```
def draw():
    screen.draw.text('A', center=(x, y), color=(128, 0, 128), fontsize=60)
```

