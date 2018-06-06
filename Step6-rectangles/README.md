We've set up a game where one letter can chase the other but we haven't yet set up anything to happen when the chasing letter catches the other letter. What we need is for Pygame Zero to check if one letter is overlapping the other, then we can write some code to show that the catch has happened.

Unfortunately Pygame Zero doesn't give us an easy way to determine when one letter is overlapping with the other. You could do it with some rather complicated maths but there is a much easier way using Rectangles.

Rectangle variables
-------------------

A Rectangle in Pygame Zero is a box which can be drawn in the window. To make a rectangle we create a new variable. The variables you have seen so far have been ones that contain numbers (numerical variables), ones that contain text (string variables), ones that can be either True or False (Boolean variables) but in fact in Python variables can be all sorts of other things which go  under the name of "objects". We are going to make a variable which is a Rectangle object.

To do this we have to use code like this:

```mybox = Rect(1st number, 2nd number, 3rd number, 4th number)```

In this code mybox is the name of the variable, Rect is a Pygame Zero key word which tells us the variable is going to contain a Rectangle object, then we have to give four numbers in brackets to define our rectangle. The first number is the x coordinate of the left edge of the rectangle, the second number is the y coordinate of the top edge of the rectangle, the third number is the width of the rectangle in pixels, and the fourth number is the height of the rectangle in pixels. In Python the numbers in brackets in code like this are called parameters.

So if my code was

```mybox = Rect(10, 20, 40, 30)```

this would make a rectangle object with the left edge at x coordinate 10, the top edge at y coordinate 20, and 40 pixels wide and 30 pixels high. Note that we've only *created* a rectangle object - we haven't done anything about *drawing* it in the window yet.

To make the rectangle move we have to change the x and y coordinates. We can do this with a statement like this:

```mybox.center=(100, 150)```

Note we have to use the American spelling of center. This would set the centre of the box at coordinates x = 100, y = 150. Or we could use numerical variables for the x and y coordinates, as we did for the letters A and B. But we still haven't drawn it in the window.

To draw it in the window we add a statement into the draw function like this:

```screen.draw.rect(mybox, color='red')```

This tells Pygame Zero to draw a box coloured red, with the height and width which we specified when we created the mybox variable, and at the x and y location which we specified last time we changed the coordinates. You can put any colour here, but you have to include a colour or you will get an error. You could also use an RGB type of colour with color=(50, 100, 150) for example.

Because our code will be constantly updating the x and y coordinates of the Rectangle it really doesn't matter what values you put in for the first and second numbers when you create the new Rectangle variable. These will be updated before the rectangle ever gets drawn.

Look at the Python code [rect1.py](rect1.py) which is included in this step. This code creates a rectangle object, and draws it in the centre of the window. It allows the rectangle to be moved by pressing the arrow keys but the code prevents the rectangle going outside the window. This code is really similar to the code for moving letter A. The main difference is that for letter A we set the x and y coordinates in function draw. But for a rectangle Pygame Zero works slightly differently, and we have to set the x and y coordinates in function update.

Challenge
=========
If you would like some practice in coding: edit the Python code rect1.py to add a second rectangle variable with its movement controlled by four keys at the left end of the keyboard. This is almost exactly what you did to add a second letter in step 5, so a lot of the steps will be almost exactly the same.

If you don't need the extra practice you can look at the code [rect2.py](rect2.py) which is included in this step. This code creates two rectangles and allows them to be moved with different keys. 

Have a look at the last two lines of function draw in this code: these two lines draw some text on the screen to give instructions to the players. These lines of text are deleted and redrawn every time Pygame Zero runs the update and draw functions, but since they are always drawn in exactly the same place it looks as if they are constantly on the screen.


[Go to step 7](../Step7-collision)