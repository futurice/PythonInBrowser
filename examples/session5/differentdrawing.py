# Learn to draw within given boundaries

##### INFO #####
# Let's import turtle, that enables drawing on the canvas
import turtle
# Random gives us nice opportunities to let the computer make
# decisions for us
import random

# So far we've given given exact orders
# for the turtle to draw lines or curves.
# This means the drawing is done without any conditions.
# Let's do a little excercise and practice drawing within specified area.

# Here we define a turtle and its speed
t = turtle.Turtle()
t.speed("fastest")
t.color("black")

# Here we calculate the size of the screen
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()
maxWidth = width / 2
minWidth = -maxWidth
maxHeight = height / 2
minHeight = -maxHeight

# Function that moves the turtle
# Note that this is just a definition, it doesn't do anything yet.
def doMove():
  # Let's store the position of the turtle in variable x and y
  x = t.xcor()
  y = t.ycor()
  # This if clause checks if we are inside the window
  if (x < maxWidth) and (x > minWidth) and (y < maxHeight) and (y > minHeight):
    # If the turtle is inside the window, it moves 10 pixels forward...
    t.forward(10)
  else:
    # If the turtle is not inside the window,
    # it turns 120 degrees right...
    t.right(120)
    # ...and moves 10 pixels forward...
    t.forward(10)

##### EXERCISE #####

# Click 'Run' and see what happens.
# Note that the only line that shows any concrete output,
# when clicking 'Run'are the uncommented lines below

# This prints the result of screen size calculations
print(maxWidth, minWidth, maxHeight, minHeight)

# And this is where we call the doMove() function repeatedly
while True:
  doMove()

# What's the benefit of drawing like this?
# Try resizing the browser window and click again 'Run'.
# The drawing works in similar manner, right?
# When we move turtle by giving conditions instead of predetermined
# lenghts and angles, we are able to make turtle move in changing conditions.
# This will hopefully prove beneficial later in the course.
