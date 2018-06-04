When we are looking at two rectangles Pygame Zero has a built-in function to detect whether or not they are overlapping. If the two rectangles objects are held in variables abox and bbox then this code:

```abox.colliderect(bbox)```

will have a value True if the rectangles are overlapping or False if they are not overlapping. Note that you would get exactly the same answer if you wrote this code instead:

```bbox.colliderect(abox)``` as in both cases it simply looks at whether the boxes are overlapping.

We can show this happening by making changes to the code [rect2.py](..\Step6-rectangles\rect2.py) in the previous step.