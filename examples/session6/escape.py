##### INFO #####

# There is a lot of code here needed for setting up the
# playing area. You can scroll down past these to the
# Exercises section.

import turtle2
import random
import time


# Generate a list of numbers from a to b at regularly spaced intervals.
def linearlySpaced(a, b, interval):
  xs = []
  x = a
  while x <= b:
    xs.append(x)
    x = x + interval
  return xs


# Generate random obstacles for the turtle.
# The obstacles are horizontal rectangles.
# n is the number of obstacles to generate.
# The obstacles are generated inside the area defined by the
# parameters left, right, top and bottom.
def generateObstacles(n, left, right, top, bottom):
  height = 20
  minWidth = round(0.1 * (right - left))
  maxWidth = round(0.8 * (right - left))

  alternatives = linearlySpaced(bottom, top, 2 * height)
  random.shuffle(alternatives)
  alternatives = sorted(alternatives[:n])

  obstacles = []
  for y in alternatives:
    x1 = random.randint(left - maxWidth + minWidth, right - minWidth)
    x = max(x1, left)
    width = random.randint(minWidth, maxWidth)
    width = min(width, right - x)

    obstacles.append((x, y, width, height))

  return obstacles


# Create rectangle parameters for the left, right and bottom sides of the area.
def outerBounds(left, right, top, bottom):
  w = 20
  return [
    (left - w, bottom - w, w, top - bottom + w),
    (left, bottom - w, right - left, w),
    (right, bottom - w, w, top - bottom + w)
  ]


# Draw a rectangle at the location (x, y). The rectangle will be w
# pixels wide and h pixels high. It will be drawn using the turtle t.
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
  t.end_fill()
  t.penup()


# Draw several rectangles.
# rectangles is a list of (x, y, width, height) variables.
def drawRectangles(rectangles):
  t = turtle2.Turtle()
  t.speed("fastest")
  t.color("red")
  t.hideturtle()
  for rect in rectangles:
    drawRectangle(t, rect[0], rect[1], rect[2], rect[3])


def drawFinishLine(x1, x2, y):
  t = turtle2.Turtle()
  t.hideturtle()
  t.speed("fastest")
  t.color("blue")
  t.pensize(3)
  t.penup()
  t.goto(x1, y)
  t.pendown()
  t.goto(x2, y)


# Returns True if the coordinate (x, y) is inside a rectangle.
def isInsideRectangle(x, y, rectangle):
  return (x >= rectangle[0] and x < rectangle[0] + rectangle[2] and
      y >= rectangle[1] and y < rectangle[1] + rectangle[3])


# Returns True if (x, y) is inside any of the rectangles in the
# provided list.
def isInsideAnyRectangle(x, y, rectangleList):
  for rectangle in rectangleList:
    if isInsideRectangle(x, y, rectangle):
      return True
  return False


# The function below will control how the turtle moves. This function
# is called continuously in a loop. It selects a new direction for the
# turtle and moves it a short distance forward.
def moveOneStep(t, obstacles):
  x = t.xcor()
  y = t.ycor()

  if isInsideAnyRectangle(x, y, obstacles):
    t.right(180)
  else:
    t.right(random.randint(-30, 30))

  t.forward(10)


# Generate obstacles at random locations by calling the helper
# functions defined above.

screen = turtle2.Screen()
right = min(250, screen.window_width() / 2 - 5)
left = -right
top = min(270, screen.window_height() / 2 - 5)
bottom = -top

obstacles = (outerBounds(left, right, top, bottom) +
       generateObstacles(4, left, right, top - 20, bottom + 60))

# Draw the obstacles
turtle2.pauseDrawing()
drawRectangles(obstacles)
drawFinishLine(left, right, top)
turtle2.unpauseDrawing()

# Create the turtle
t = turtle2.Turtle()
t.speed("fastest")
t.penup()
t.goto((left + right) / 2, bottom + 20)
t.setheading(90)
t.pendown()

# This loop moves the turtle one step at a time until it reaches the
# top.
startTime = time.time()
while t.ycor() < top:
  moveOneStep(t, obstacles)
endTime = time.time()

print "The turtle reached the finish line in %d seconds!" % round(endTime - startTime)


##### EXERCISE 1 #####

# The goal is to move the turtle to the blue finish line at top without
# crossing over any red obstacle.
#
# Press 'Run' and see what happens. Will the turtle reach the top
# of the screen and how long does it take?
#
# Try to understand how the moveOneStep function controls turtle's
# movement.
#
# When you press 'Run' again, new obstacles will be generted at random
# locations.

##### EXERCISE 2 #####

# It can take a rather long time for the turtle to get to the finish
# line because it chooses the movement directions randomly.
#
# Modify the moveOneStep function so that the turtle sometimes selects
# a new direction randomly (like before) but sometimes moves upwards.
# You can use the following command to set the direction upwards:
#
# t.setheading(90)
#
# Will the turtle reach the finish line faster?

##### EXERCISE 3 #####

# Try to come up with other movement styles and change the
# moveOneStep function accordingly.
#
# For example: only change the direction if the turtle hits an
# obstacle, otherwise move in straight lines.
#
# What is the fastest way to finish?

#### ADDITIONAL EXERCISE #####

# Change the obstacle shapes by modifying the generateObstacles
# function. You can, for example, try vertical bars or squares.
#
# You can also try circles, but then you need implement functions for
# drawing and collision detection. Use the drawRectangles and
# isInsideRectangle functions, which draw and do collision testing for
# rectangles, as starting points.
