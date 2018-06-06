If your code is working fine so far a good suggestion, at this stage, is to use Save As... to save it with a new name. Then do the edits in this step in the code with the new name. That way you will still have the previous version to go back to in case any of the latest edits go wrong.

Testing if the letter is visible
--------------------------------

You may have noticed that if you keep pressing one of the arrow keys the letter will disappear out of the window. This step shows how to stop this happening, so that the letter is always visible.

Our Python code can't actually look at the screen and see if the letter is in the window but it can work out whether it's visible or not by checking what its x and y coordinates are.

Look at the picture in step 1 to remind yourself how the coordinates of the window work. 

We can see that if the letter is at the right edge of the window its x coordinate is 639. So if its x coordinate is greater than 639 we know that it will be outside the window to the right. So with our **if** statement we want to check not only if the right arrow is being pressed, but also if the letter is about to go outside the window. If it is at the edge of the window or beyond we want the right arrow to stop working.

As with all coding there are many different ways of getting the same result but a way of getting this result is to use the **if** statement to check for *two* conditions at the same time using the Python key work **and**. And one good way of arranging this is to check if the right arrow is being pressed **AND** if the letter is not outside the window to the right. If it is not outside the window to the right then the x coordinate will be 639 or less. So our if statement becomes:

```
if keyboard.right and x <= 639:
    x = x + 1
```

The code ```<=``` means 'is less than or equal to'. So the if statement will increase the x coordinate by 1 **IF** the right arrow is being pressed **AND** if the letter is not outside the window to the right. But if only one of those conditions is true, or if neither of them is true then the x coordinate won't be increased and the letter won't move to the right.

If you set up the code like this, then decided to change the size of your window it might not work properly anymore, because the coordinate of the right edge of the window might not be 639 any more. So a better way of writing the code is to make use of the global variable WIDTH, which is equal to 640 is this example code. You can draw a diagram to show yourself that whatever you changed the WIDTH to, the x coordinate of the right edge of the window would ALWAYS be one less than the value of WIDTH. The if statement then becomes:

```
if keyboard.right and x < WIDTH:
    x = x + 1
```
Remember, as WIDTH is a global variable you will need to include an extra line in the update function to prevent an error. (Can you remember what that would be?)

The Python code [letterA3.py](letterA3.py), included with this step, shows how the code might look at this stage.

Challenge
=========
What would the x coordinate be if the letter was outside the window to the left? Look at the picture in step 1 to check this. How could you write an if statement to check if the letter is not outside the window to the left?

Challenge
=========
Now edit all the other if statements so each of them will only change the coordinate if the letter is inside the window. All four will look similar to the one above but will have some important differences. Run your new code with pgzrun to test that the letter stops at the edge of the window in all four directions.

[Go to step 5](../Step5-two_letters)
