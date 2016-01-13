# differentdrawing.py
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
    # ...and calls again this same function
    doMove()
  else:
    # If the turtle is not inside the window,
    # it turns 120 degrees right...
    t.right(120)
    # ...and moves 10 pixels forward...
    t.forward(10)
    # ...and calls again this same function
    doMove()

##### EXERCISE #####

# Click 'Run' and see what happens.
# Note that the only line that shows any concrete output,
# when clicking 'Run'are the uncommented lines below

# This prints the result of screen size calculations
print(maxWidth, minWidth, maxHeight, minHeight)
# And this is where the doMove function is called for the first time
doMove()

# What's the benefit of drawing like this?
# Try resizing the browser window and click again 'Run'.
# The drawing works in similar manner, right?
# When we move turtle by giving conditions instead of predetermined
# lenghts and angles, we are able to make turtle move in changing conditions.
# This will hopefully prove beneficial later in the course.

# ADDITIONAL EXERCISE #####
# Why do we exceed the 'Maximum call stack size'?
# Take a moment and think what happens.

# We are calling the same function over and over again.
# This coding environment (like all computers) have limitations.
# When a function is called, it's added in a 'Call stack',
# and 'Call stack' has limited space in the computer's memory.
# When we call the same function over and over again,
# the call stack is constantly growing until we hit a limit,
# and execution of the program stops.

# This is normal behavior for computers. The more you deal with them,
# the more you get to understand its limitations like this.
