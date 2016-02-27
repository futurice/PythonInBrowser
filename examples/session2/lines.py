# Drawing lines

import coordinates
import turtle

coordinates.prepareCoordinates()
t = turtle.Turtle()

##### INFO #####
# The equation of line is usually given in format y = kx + b in mathematics
# We'd like to draw a line with our turtle to the canvas. So we have to write
# the equation in a format that code can understand.
# We'll do it with a function called line

def line(k, b):
    # We take penup
  t.penup()

  # for x ranging from -550 to 550 we'll do the following
  for x in range(-550, 550):
        # we go to point (x, k*x + b)
    t.goto(x, k * x + b)
        # We put pendown to start drawing
    t.pendown()

# Let see, how this works: Let's draw line y = 2x
# We'll do it like this
line(2, 0)

##### EXERCISE #####
# 1. Draw line y = -0.5 x + 50
line(-0.5, 50)

# 2. Draw line y = x - 100
line(1, -100)

# 3. Draw line of your choice
# Write first the equation and then call the function line with your values
