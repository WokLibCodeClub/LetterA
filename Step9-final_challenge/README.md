What would you like to happen when one letter catches the other?
----------------------------------------------------------------

At the moment all that happens when the two letters overlap is that you have some text on the screen which changes. Your code probably does this already, but you can see this happening with the code [textbox1.py](textbox1.py) which is included in this step. But this is not a very exciting thing to happen. 

This is where you can be creative and design your own ending to the game. See if you can come up with some ideas.

Display the word BANG?
----------------------

To give you one suggestion: maybe when the letters collide the game could stop and the word BANG! could appear across the screen in big red letters. This is what happens in the code [chase1.py](chase1.py) included with this step, so it's worth taking a moment to explain different parts of this code. 

This code is very similar to the code in [textbox1.py](textbox1.py). The most important difference is in function update. When we had code that displayed text in the window to show whether there was a collision or not we wanted to be able to keep moving the letters using the keys, even if there was a collision. But now, when there is a collision, we want the letters to stop moving. 

This is done by making changes in the if statement which tests for a collision. If there is a collision we want the things to happen which mean the game is ending, but if there is no collision we want to continue moving the letters with the keys. So in this if statement the code which comes after 
```
if collision:
```    
will be for things that happen when the game ends, while the code which comes after 
```
else:
```    
will be what happens where there is no collision - which is that the letters can continue to be moved. So to achieve this we take all the code which moves the letters, and the code which sets the coordinates for the centres of the two rectangles, INDENT it all, and put it directly underneath ```else:```, so it becomes part of the first if statement. Notice that we now have if statements *INSIDE* other if statements. This is very normal in coding, and in Python it is the indenting which enables Python to keep track of which code is part of which if statement.

You will see that under the line 
```
if collision:
```
there is another if statement. This is checking whether keyboard key x is pressed. If it is pressed then the code goes on to the next line which is ```exit()``` which is the command to quit the programme.

Remember that when we run this code with Pygame Zero it is constantly running function update, then function draw, so if the letters are colliding, every time it runs function update it will go into the first part of this if statement and check if key x is pressed. If key x is pressed the programme will exit, but if key x is not pressed it won't do anything.

The other important change is in function draw where there is now an if statement at the end of this. When Pygame Zero runs function update it checks if the letters are colliding, and if they are it sets the Boolean variable called collision to be True. Pygame Zero then goes on to function draw, where it clears the screen, draws the letters at the most recent positions, then if collision is True it writes the text 'BANG!' in large red letters, and also puts smaller text saying 'Press x to exit' in the bottom left corner. But if collision is False it ignores these lines.

To understand this code properly it is an idea to go through it in the same order that Python will go through it, remembering what value each variable will have at each step.

You could now rewrite your own code to do something like this.

Restarting the game instead of quitting
---------------------------------------

A slightly more complicated version of this would be instead pressing x to quit the programme when one letter catches the other you could press x to have the game go back to the starting positions so you can play again. This is what happens in the code [chase2.py](chase2.py) with this step, so here is some explanation of how this code works. 

In this code we have defined a new function which is called startup. We have moved some code into this function from the main part of the programme. The code which has been moved is the code which sets the starting positions of all the coordinate variables of the two letters, and the starting positions of the two rectangles.

We want to run this function firstly at the beginning of the game, and again every time there is a collision and key x is pressed. As this is not function draw or function update it will not be run automatically by Pygame Zero, so we need to add code to run this function ourselves. The line of code which runs this function is ```startup()``` which you will find just above function update. The technical term is to "call" the function.

The positioning of this line of code makes a very important point about how you arrange your Python code: *YOU MUST DEFINE A FUNCTION IN THE CODE BEFORE YOU CALL IT*. Otherwise Python will give an error.

Another change is in function update: in the statement where we check if key x has been pressed we don't want to exit the programme, we want to do something different - we want to set the programme back to its starting situation. The first thing we must do is to call our new function startup() to set the textboxes back to their starting positions. Now the game is ready to play again.

The last change to make is in function draw: where we drew the text 'Press x to exit' we now want to draw the text 'Press x to restart'.

Challenge
=========
Perhaps you could combine this with chase1.py to give the players a choice when one letter catches the other - press one key to restart the game, and a different key to exit. How would you do that?

Adding a game timer
-------------------

The code in [chase3.py](chase3.py) is based on chase2.py but has added a game timer, to time how long the letter being chased can avoid being caught. Look at the code to see how it works. One possible addition to this code would be to add a variable for the best (longest) time so far and display this.

The final challenge
-------------------

The next part is up to you. Using the different parts of Pygame Zero in this project you will be able to adapt your code to do many different things, and you can look at the full instructions for Pygame Zero, with all the different possibilities, on the webpage:

[http://pygame-zero.readthedocs.io/en/stable/index.html](http://pygame-zero.readthedocs.io/en/stable/index.html)

