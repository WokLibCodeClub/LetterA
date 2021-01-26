Hopefully you managed to get your code to work in the previous step, even if it didn't work first time. You can learn an awful lot about coding by successfully debugging your code. In case you got completely stuck you can look at [rect3.py](rect3.py) which is included in this step to see one example of it working, then compare this with your version to see if it helps you to get your version to work.

Textboxes
---------

Pygame Zero has a lot of special functions for displaying objects in the game window, which you can put inside function draw.

We've already seen

```screen.draw.text``` which displays some text or a text variable and ```screen.draw.rect``` which draws a box.

But there are also

```screen.draw.filled_rectangle``` which draws a box and fills it with colour  
```screen.draw.line``` which draws a line when you give it coordinates for the beginning and end  
```screen.draw.circle``` which draws a circle when you give it the position and size  
```screen.draw.filled_circle``` which draws a circle and fills it with colour  
```screen.draw.blit``` which draws an image from an image file on the screen  

You can find a complete list with all the necessary instructions on how to use them at:

[http://pygame-zero.readthedocs.io/en/stable/builtins.html#screen](http://pygame-zero.readthedocs.io/en/stable/builtins.html#screen)

In this section we're going to use

```screen.draw.textbox``` which is very similar to ```screen.draw.rect``` but instead of drawing a box it fills the box with text or a text variable.

The way to use this is to put code like this in function draw:

```python
screen.draw.textbox('A', abox, color='red')
```

This uses a rectangle which has already defined - in this example it is a variable called abox - but instead of drawing the box it puts the letter A inside the box and draws that.

One important thing about ```screen.draw.textbox``` is that it automatically scales the text to fit in the rectangle. So **you can't use fontsize= with a textbox**, as the text size is controlled by the size of the rectangle. It also means if your text is long, you should make your rectangle wider than it is high to fit the text you want to display in it.

There doesn't seem to be a way to display a textbox *AND* have the box drawn as well. So one way you could do this is by having two draw statements:

```python
screen.draw.textbox('A', abox, color='red')
screen.draw.rect(abox, color='red')
```
The first statement draws the letter A in a red colour inside the rectangle called abox, and the second statement draws the outline of the rectangle abox, also in red. Since we haven't changed the coordinates of abox both the letter A and the red outline will be drawn at exactly the same location.

Changing your rectangles to textboxes
------------------------------------

You can now make some small adjustments to your code from step 7 to change your rectangles into text boxes. All you have to do is change the ```screen.draw.rect``` commands to ```screen.draw.textbox``` and add the text which you want display in each rectangle as the first parameter inside the brackets.

If you want to make the displayed text bigger or smaller you can do this by changing the size of the rectangles, which you do in the line of code where you created (or *declared*) the rectangle variables.

You should now have code which will have two letters moving about in the game window, controlled by different keys, and a way of testing when the letters are overlapping, which would happen when one letter catches the other.

But what would you like to happen when one letter catches the other?


[Go to step 9](../Step9-final_challenge)
