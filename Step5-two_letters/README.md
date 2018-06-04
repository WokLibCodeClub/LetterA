Hopefully you now have code which allows you to control a letter around the screen using the arrow keys but which will not go outside the window in any direction. A good suggestion is to use Save As... to save this code with a new name and do the next lot of editing in the new file.

We are going to make a game in which two players can sit at the same keyboard and control *TWO* letters, with one letter chasing the other.

To do this you need to expand your code to create a second letter, this time controlled by keys at the left-hand edge of the keyboard (you can choose which keys you like for this). This will make your code almost twice as long.

Here are some things to bear in mind:

* your two letters need to move independently, so each letter needs its own variables for its x and y coordinates
* you can only have one function called update and one function called draw, otherwise Pygame Zero will be confused and won't know which function to run, so all the update code for both letters needs to go in function update, and all the drawing code for both letters needs to go in function draw
* to test if, for example, the letter x is being pressed use the Pygame Zero code keyboard.x. The pattern is the same for any other key you want to use to move your letters

[Go to step 6](../Step6-rectangles/README.md)
