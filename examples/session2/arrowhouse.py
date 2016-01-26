##### FILE #####
# arrowhouse.py
# Let’s practice being architects and draw a house.

##### INFO #####
# Importing turtle and assigning it to a variable ’t’.
import turtle
t = turtle.Turtle()

# By now you might remember that Turtle is a way we can draw on the canvas.
# Below we are first defining the length of the wall of the house.
# To have a proper length for the roof we can use a ratio of 1:5.
# Let's assign that in a variable called 'gutter'.

wall = 50
gutter = wall / 5

# We are first moving the turtle forward the length of wall,
# turning it left 90 degrees and moving it forward the length of wall
# then turning right 90 degrees, going forward the length of gutter,
# which is one fifth of the length of the wall,
# then turning left 135 pixels and finally going forward the length of the wall again.

t.forward(wall)
t.left(90)
t.forward(wall)
t.right(90)
t.forward(gutter)
t.left(135)
t.forward(wall)

##### EXERCISE #####
# Click 'run' and see what happens.
# There’s half of a house drawn on the canvas.
# Finalise the house by adding proper turtle commands above,
# below the commands that are already there.
# HINT: it takes 6 more rows to complete the house.
# You can always click ‘Run’
# and test if you’re moving the turtle in a proper direction.
# HINT2: It's wise to use the variables 'wall' and 'gutter' for going forward.

# When the house is completed, you might ask
# whether it looks more like a house or an arrow.
# Perhaps that's just a matter of taste.

# Using a ratio as a value for the length of the gutter gives us
# the advantage that it's easy to draw the house in different sizes.
# Change the value of wall to something between 10 and 150 and check
# that the drawing still works.

# Then as a final thing, try changing the value of wall to 500, click 'Run'.
# Wait for a little while until the turtle arrow comes back on the screen.
# You see that the arrow doesn't exactly meet with the line. The ratio isn't perfect.

# You could ask your math teacher how and why this happens.
# What would be the correct way to calculate the length of the gutter?
