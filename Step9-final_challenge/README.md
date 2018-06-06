What would you like to happen when one letter catches the other?
----------------------------------------------------------------

At the moment all that happens when the two letters overlap is that you have some text on the screen which changes. Your code probably does this already, but you can see this happening with the code [textbox1.py](textbox1.py) which is included in this step. But this is not a very exciting thing to happen. 

This is where you can be creative and design your own ending to the game. See if you can come up with some ideas.

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

Remember that when we run this code with Pygame Zero it is constantly running function update, then function draw, so if the letters are colliding every time it runs function update it will go into the first part of this if statement and check if key x is pressed, but it won't do anything if key x is not pressed.

The other important change is in function draw where there is now an if statement at the end of this. When Pygame Zero runs function update it checks if the letters are colliding, and if they are it sets the Boolean variable called collision to be True. Pygame Zero then goes on to function draw, where it clears the screen, draws the letters where they were before the collision, then if collision is True it writes the text 'BANG!' in large red letters. But if collision is False it ignores this line.

Other possibilities
-------------------

Here are some other things you could put into your code:

* Instead of the game quitting when one letter catches the other you could have the game go back to the starting positions so you can play again. This is what happens in the code [chase2.py](chase2.py) with this step. One way to do this is to make a new function which sets the initial posision