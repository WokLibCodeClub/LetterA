What would you like to happen when one letter catches the other?
----------------------------------------------------------------

At the moment all that happens is that you have some text on the screen which changes when the two letters overlap. But this is not a very exciting thing to happen. 

This is where you can be creative and design your own ending to the game. The code [chase1.py](chase1.py) included with this step shows one possible ending, so it's worth taking a moment to explain different parts of this code.

The key difference in the coding is in function update. When we had code that displayed text in the window to show whether there was a collision or not we wanted to be able to keep moving the letters using the keys, even if there was a collision. But this code has been written so when there is a collision the letters can't be moved any more. 

This is done with the if statement in function update, which in words does this:
```
if collision:
    

Other possibilities
-------------------

Here are some other things you could put into your code:

* Instead of the game quitting when one letter catches the other you could have the game go back to the starting positions so you can play again. One way to do this is to make a new function which 