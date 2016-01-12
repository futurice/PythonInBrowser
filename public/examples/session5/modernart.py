# modernart.py
# Learn to read code, understand functions and randomization
import turtle
import random

t = turtle.Turtle()

boundX = 180.0
boundY = -180.0

# This function draws two squares as a frame to our modern art painting
# In the end, it calls the function 'doMove' for the first time.
def initializeModernArt():
  t.penup()
  t.goto(-220, -220)
  t.pendown()
  square(440)
  t.penup()
  t.goto(-180, -180)
  t.pendown()
  square(360)
  t.penup()
  t.goto(0,0)
  t.right(35)
  t.pendown()
  t.color("green")
  doMove()

# This function draws a square
def square(side):
  for i in range(0, 4):
    t.forward(side)
    t.left(90)

# This function is called when we are out of boundaries.
# Check comments inside the function
def collision():
  x = t.xcor() #  x coordinate of our turtle
  y = t.ycor() #  y coordinate of our turtle

  # Check if we are more that 15 away from inner border
  if ((x > boundX) & (x - boundX > 15)) | ((x < boundY) & (boundY - x > 15)) | ((y > boundX) & (y - boundX > 15)) | ((y < boundY) & (boundY - y > 15)):
    # if we are we call 'majorCollision' function
    majorCollision()
  else:
    # if we are not we call 'minorCollision' function
    minorCollision()

# Function that handles minor collision
def minorCollision():
  angle = random.randint(20, 70) #  random value between 20 and 70
  t.color("blue")
  t.right(angle)
  t.forward(10)
  doMove()

# Function that handles majorCollision
def majorCollision():
  step = 30
  t.color("red")
  t.right(175)
  t.forward(30)
  doMove()

# Function that does moving of turtle
def doMove():
  x = t.xcor()
  y = t.ycor()
  # Let's check if we are inside boundaries
  if (x <= boundX) & (x >= boundY) & (y <= boundX) & (y >= boundY):
    t.color("green")
    t.forward(10)
    doMove()
  else:
    # If we are not inside boundaries we'll call 'collision' function
    collision()

# This is the first actual function call in our programm
initializeModernArt()
