Detecting a collision
---------------------

When we have two rectangles Pygame Zero has a built-in function to detect whether or not they are overlapping. If the two rectangle objects are held in variables abox and bbox then this code:

```abox.colliderect(bbox)```

will have a value True if the rectangles are overlapping or False if they are not overlapping. Note that you would get exactly the same answer if you wrote this code instead:

```bbox.colliderect(abox)``` as in both cases it simply looks at whether the boxes are overlapping.

A good way to demonstrate this is to change the code [rect2.py](../Step6-rectangles/rect2.py) which was included in step 6, so that as we move the two rectangles around it will display some text to tell us if the boxes are overlapping or not. 

Below are some instructions which show one way to achieve this.

Suggestion: Use Save As    to save the code rect2.py with a new name and make your edits in the file with the new name.

Challenge
=========

These instructions don't give every detail about how to make the changes. The challenge is to use your knowledge of Python and think how the code is running to make sure you put all the new code in the right place. There are some suggestions and hints included.

If you try to run your new code with pgzrun and it doesn't work pay close attention to the error messages in the terminal window. The last line of the messages usually points to the exact line in your code where Python found a problem. This will help you find where you might need to make changes.

1. If we want to keep track of whether the rectangles are overlapping or not a good way is to make a global variable which would be either True if they are overlapping or False if they are not. So start by making a new global variable and set it equal to False. (By doing this we immediately signal to Python that the new variable is a Boolean type variable which can be either True or False but can't have any other value.) You can choose what to call the variable. It would make sense to put the code for this variable with the code which creates our other global variables.

2. We are going to display some text in the game window to show if the rectangles are overlapping or not, and we want this text to be different depending on whether they are or aren't overlapping. A good way to do this is to put the text in a text variable. So you will need to make another new global variable, which will be a text variable. You tell Python that your new variable is a text variable by setting it equal to something in quotes. It doesn't matter what initial value you give it, as long as it's in quotes, as you will be changing the value later in the programme.

3. The place to test whether a collision is occurring is in function update, and we are going to use both of our new global variables in function update. So what do you need to add to the beginning of function update first, to prevent a scope of variables error?

4. In function update we will use the code ```abox.colliderect(bbox)``` to test if the rectangles are overlapping. This code will give a value of True or False. So, in function update, put a line of code which will set your new Boolean variable equal to ```abox.colliderect(bbox)```. 

5. We are now going to put a new if statement in function update. This will be slightly more complicated than the if statements we've used so far, as we want to give it two possible outcomes.

   The if statement will look something like this (pay special attention to how the indents work):
   ```
   if something or other is true:
       do one thing
   else:
       do something different
   ```
   By using the Python key word ```else``` we can give an instruction for what to do if the thing we are testing is NOT true.

   The "something or other" that we want to test is the new Boolean variable, and when we are testing a Boolean variable the if line is quite simple and consists of just the word 'if', and a space, and the name of the Boolean variable, then a colon.

   If the Boolean variable is true, it means the rectangles are overlapping. And the 'do one thing' line will set the new text variable to contain some text which explains that the rectangles are colliding.

   If the Boolean variable is not true, it means the rectangles are not overlapping. And the 'do something different' line will set the new text variable to contain some text which explains that the rectangles are not colliding.

6. The last step is to display our new text variable, which we do in function draw. At the end of code rect2.py there are two lines which display text near the bottom of the window. You can delete one of these, but change the other one so that instead of displaying some text in quotes it will display your new text variable, without any quotes. You can adjust the exact position in the window where the centre of the text is located by changing the code in the brackets after center=.

