# Create a Pygame Zero window and draw a letter

When you run code using Pygame Zero (which you do by typing ```pgzrun <name of python programme>.py``` in a command window) a lot of things happen behind the scenes which you can't see.

Firstly, Pygame Zero creates a window for your code to operate in. In fact, even if you make a completely empty Python programme which has no text in it at all, then run it with *pgzrun*, Pygame Zero will create a window.

## Make a folder for your project

It's a good to make a folder for this project so that you can keep all the different bits of code together.

## Create a new python file

You'll want a Python file (with an extension .py) to write your code in.

If you're using Python IDLE as the Python editor go to File>New File, then in the new window select File>Save As... and save your new file (you could call it letterA.py) in your project folder. You should now open a Command Window and change the directory until you are in your project folder. In the command window you can type ```pgzrun letterA.py``` and you should see a window appear. Kill the window by clicking the red cross in the top right corner.

If you're using Visual Studio Code, when you open the programme select File>Open Folder to open your project folder, (instead of File>Open File). The left edge of the screen will then show a list of all the files in your folder (there aren't any yet). Use File>New File to create a new editing window, then click File>Save As..., and give the new file a name, and make sure you select 'Python' from the list in the box 'Save as type:'.
Now go to View>Integrated Terminal and it should open a new terminal window at the bottom, which is already set to your project folder. In this window you can type ```pgzrun letterA.py``` (if you called your file letterA.py) and it should display a window. Kill the window by clicking the red cross in the top right corner.

## Controlling the window size

We can control the size of the Pygame Zero window by adding code like this into the .py file:

```python
WIDTH=800
HEIGHT=600
```

Pygame Zero will use these commands to make a window which is 800 pixels wide and 600 pixels high. By changing the numbers you can make a window any size you want. But although ```WIDTH``` and ```HEIGHT``` have special meanings for Pygame Zero they are also just normal Python numerical variables, which means you can also use them in calculations.

When Pygame Zero makes a window it also creates a coordinate system to allow you to place objects in the window at the position you want. The x coordinate starts at 0 at the left edge of the window and increases to the right. If your window is 800 pixels wide then the extreme right edge of the window will have an x coordinate of 799.

The y coordinate starts at 0 at the top edge of the window and increases DOWNWARDS. __*Be careful!*__ This is the opposite way round to coordinate systems in Scratch, or Python turtle windows, or in normal graphs you might draw in maths. If your window is 600 pixels high then the extreme bottom edge of the window will have a y coordinate of 599.

![coordinates](window.png "Coordinate system")

## Displaying something in the window

If we want to display something in the window we need to create a function with the name ```draw```. We define this function like this:

```python
def draw():
```

Pygame Zero always looks for a function called ```draw()```, and when it finds one it starts executing it over and over again, very fast (60 times a second). It does this behind the scenes without you having to write any code.

To display a letter A in the window, with its centre at coordinates x = 100, y = 100 we need to put this code in the ```draw()``` function:

```python
    screen.draw.text('A', center=(100,100))
```

Don't forget that this line needs to be *indented*, so that Python knows it is part of the ```draw()``` function and not part of the rest of the code. Note also that Python commands are based on the spelling of American English, which means we have to use the American spelling "center" instead of the British "centre".

**Save** your file, and run it using pgzrun, to check that a letter appears. You will have to kill the window by clicking on the red cross in the top right corner before you can continue.

## Challenge 1

Use what you know about the coordinate system to get the letter A (or whatever letter you like) to appear exactly in the centre of your window. You can do this by changing the numbers in the part of the code which says ```center=(100,100)```.

If you have made the letter appear in the centre of the window you might have done some division sums. But if you decided you wanted to change the size of the window would the letter still be in the centre?

## Challenge 2

Change your code so that the letter will appear in the centre of the window whatever size of window you choose. Remember that ```WIDTH``` and ```HEIGHT``` are Python variables, so you can use them in calculations.

If you manage to solve this you should also be able to change the coordinates to make the letter appear in the bottom right of the window, or the top left, or bottom left or wherever you want, and have this work even if you change the window size.

[Go to step 2](../Step2-move_letter)
