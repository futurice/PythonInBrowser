# Turtle moving around cubes

##### INFO #####
import turtle
import turtle2
import random

# Here we define a turtle and its speed
t = turtle.Turtle()
t.speed("fastest")
t.color("black")

# Here we calculate the size of the screen
screen = turtle.Screen()
screen.bgcolor("blue")
width = screen.window_width()
height = screen.window_height()
maxWidth = width / 2
minWidth = -maxWidth
maxHeight = height / 2
minHeight = -maxHeight

def blend_colors(color1, color2, weight1=1.0, weight2=1.0):
  u = weight1/(weight1 + weight2)
  v = weight2/(weight1 + weight2)
  return (u*color1[0] + v*color2[0],
          u*color1[1] + v*color2[1],
          u*color1[2] + v*color2[2])

def draw_block(t, x, y, color=(255, 0, 0), size=50):
  turtle2.pauseDrawing()
  t.speed("fastest")
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.setheading(90)
  t.pendown()

  # The right side
  t.fillcolor(blend_colors(color, (0, 0, 0)))
  t.begin_fill()
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.end_fill()

  # The left side
  t.fillcolor(blend_colors(color, (0, 0, 0), weight1=3.0))
  t.begin_fill()
  t.right(60)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.end_fill()

  # The top side
  t.fillcolor(color)
  t.begin_fill()
  t.right(180)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.end_fill()

  turtle2.unpauseDrawing()

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

    draw_block(t, x, y)
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

def doMove():
  rectangles = generateObstacles(10)

  while True:
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

# Remember the obstacles exercise? This is modification of it.
# The rectancles have been changed with cubes.
# How ever the exercise hasn't been modified enough.
# Note that the boundaries of cubes are different that boundaries of rectancles.
# See below things you can fix in this exercise.

# This will start the animation.
t.penup()
doMove()

# 1. Fix the boundaries so that turtle can't go inside cubes.

# 2. Change the background color to the one you want

# 3. Choose the color of cubes randomly

# 4. Can you also add a finish line like in the exercise 1 in the session 6?

