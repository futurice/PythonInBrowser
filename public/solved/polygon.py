##### FILE #####
# polygon.py
# Learning to draw polygons with functions

import turtle
t = turtle.Turtle()

##### INFO #####

# Here we have a function that defines triangle
# It takes one variable 'side'.
# 'Side' defines the length of the side in triangle
# Read the code, explain to your friend what is happening in each line

def triangle(side):
  for i in range(0, 3):
    t.forward(side)
    t.right(120)

##### EXERCISE #####

# 1. Let's draw triangles: Use the function triagle with different values of side.

# 2. Next, write a function that draws a square. Look for the triangle-function for help.
# How much do you turn now after moving forward?
# After writing the function draw few squares with different values of side

def square(side):
  for i in range(0, 4):
    t.forward(side)
    t.right(360/4)

# 3. Let's draw a pentagon! Make a function that draws a pentagon and use it.

def pentagon(side):
  for i in range(0, 5):
    t.forward(side)
    t.right(360/5)

# 4. Let's draw a polygon!
# Could you write a function, that draws any kind of regular polygon?
# Look at the functions triangle, square and pentagon, what do you notice?

def polygon(numberOfSides, side):
  for i in range(0, numberOfSides):
    print i
    t.forward(side)
    t.right(360.0/numberOfSides)
