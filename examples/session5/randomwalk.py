# Turtle moving around obstacles

##### INFO #####
import turtle
import random

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

def drawRectangle(t, x, y, w, h):
  t.penup()
  t.setheading(0)
  t.goto(x, y)
  t.pendown()
  t.begin_fill()
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.end_fill()
  t.penup()

def generateObstacles(n):
  t = turtle.Turtle()
  t.speed("fastest")
  t.color("red")
  
  rectangles = []
  for i in range(n):
    x = random.randint(-maxWidth, maxWidth)
    y = random.randint(-maxHeight, maxHeight)
    w = random.randint(10, 300)
    h = random.randint(10, 300)
    
    drawRectangle(t, x, y, w, h)
    
    rectangles.append((x, y, w, h))
    
  t.hideturtle()
  return rectangles
    
def isInsideRectangle(x, y, rectangle):
  return (x >= rectangle[0] and x < rectangle[0] + rectangle[2] and
      y >= rectangle[1] and y < rectangle[1] + rectangle[3])

def isInsideAnyRectangle(x, y, rectangleArray):
  for rectangle in rectangleArray:
    if isInsideRectangle(x, y, rectangle):
      return True
  return False

def isOutsideScreen(x, y):
  return x < minWidth or y < minHeight or x >= maxWidth or y >= maxHeight

def doMove(rectangles):
  x = t.xcor()
  y = t.ycor()
  
  if isOutsideScreen(x, y):
    t.right(180)
  elif isInsideAnyRectangle(x, y, rectangles):
    t.right(180)
  else:
    t.right(random.randint(-30, 30))
    
  t.forward(10)

##### EXERCISE #####

# Click 'Run' and see what happens.
# Press 'Run' again to get a different set of rectangles.
# If the turtle gets stuck right at the start, press 'Run' again.

rectangles = generateObstacles(10)

# This will start the animation.
while True:
  doMove(rectangles)

# 1. Modify the doMove function so that instead of avoiding the
# rectangles the turtle can move inside them but only in a straight
# line.

# 2. Modify the doMove function so that the turtle always does
# t.right(10) when inside a rectangle.

# 3. Modify the doMove function so that the first time the turtle
# moves inside a rectangle it keeps moving inside the rectangle
# forever and never moves out of the rectangle again.

##### ADDITIONAL EXERCISE #####

# Replace the generateObstacles() function with your own function
# that draws a labyrinth instead of random rectangles. Can the turtle
# find a way out of the labyrinth?
