When we are looking at two rectangles Pygame Zero has a built-in function to detect whether or not they are overlapping. If the two rectangles objects are held in variables abox and bbox then this code:

```abox.colliderect(bbox)```

will have a value True if the rectangles are overlapping or False if they are not overlapping. Note that you would get exactly the same answer if you wrote this code instead:

```bbox.colliderect(abox)``` as in both cases it simply looks at whether the boxes are overlapping.

We can show this happening by making some changes to the code [rect2.py](../Step6-rectangles/rect2.py) in the previous step.

Try to put in these changes using just the instructions here. You will have to use your Python knowledge to make sure your code makes sense.

1. Create a global variable called collision and give it a value ```False```. Put this in the top part of the code with other global variables. This is a variable which we will use to record whether the two rectangles are overlapping. It is a type of variable called a Boolean variable which can be either True or False but can't have any other value.
2. Create another global variable called coll_text and give it the value ```'collision = False'```. By putting the value in quotes like this we are telling Python that this is a string or text variable.
3. We have just made two more global variables which we are going to use in function update. So we need to expand the line beginning global to include the two new variables.
4. Below the global statement in function update put this:
```collision = abox.colliderect(bbox)```. This statement tests whether the rectangles are overlapping and puts the answer in our Boolean variable called collision.
5. Underneath the collision statement make an if statement. This statement has to set the variable coll_text to contain 'collision = True' if variable collision is True, or 'collision = False' if collision is false.
6. In function draw replace the last two lines with one line which will display the variable coll_text.

