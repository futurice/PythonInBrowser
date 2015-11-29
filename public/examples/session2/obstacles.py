##### FILE #####
# obstacles.py
# Find a route through obstacles

import turtle

##### INFO #####

# This code draws the obstacles and the goal.

wall = turtle.Turtle()
wall.hideturtle()
wall.speed(0)
wall.width(3)
for x in [-180, -20, 140]:
  wall.penup()
  wall.goto(x, -500)
  wall.pendown()
  wall.goto(x, 120)
  wall.penup()
  wall.goto(x, 230)
  wall.pendown()
  wall.goto(x, 500)
  
  x2 = x + 80
  wall.penup()
  wall.goto(x2, -500)
  wall.pendown()
  wall.goto(x2, 20)
  wall.penup()
  wall.goto(x2, 100)
  wall.pendown()
  wall.goto(x2, 500)
  
wall.penup()
wall.goto(250, -70)
wall.dot(20, 'red')

tess = turtle.Turtle()
tess.speed(0)
tess.penup()
tess.goto(-260, 0)
tess.pendown()
tess.speed(6)

##### EXERCISE #####

# Guide Tess the turtle to the red dot. Don't touch the wall!
#
# Expand the following code. You can make Tess to repeat part of the
# path by changing the number in range(1) from 1 to something else.

tess.left(90)
tess.forward(70)
tess.right(135)

for i in range(1):
  tess.left(90)
  tess.forward(115)
  tess.right(90)
  tess.forward(115)
