##### FILE #####
# perimeter2.py
# Computing a circumference

##### INFO #####
# How long is a distance around a circle? We get an approximate answer
# by drawing a regular polygon inside the circle and measuring the
# distance along the polygon's perimeter. When the number of polygon's
# sides is increased, it approximates the circle better and better.
#
# The distance around the circle is called a circumference.

# The following code setups the screen for the exercise.

import turtle
from math import cos, sin,  pi, sqrt

# Draw a circle
r = 200
circle = turtle.Turtle()
circle.speed('fastest')
circle.hideturtle()
circle.penup()
circle.color('red')
circle.goto(0, -r)
circle.pendown()
circle.circle(r)

# This function draws a regular polygon inside the circle. The
# parameter n controls how many sides the polygon has. The function
# returns the perimeter of the polygon.
def polygon(n):
  # Setup the turtle
  t = turtle.Turtle()
  t.penup()
  t.speed('fastest')
  t.goto(0, r)
  t.right(180.0/n)
  t.speed(6)
  t.pendown()

  # Compute the side length of the polygon
  step = 2 * r * sin(pi/n)

  # Draw the polygon and record its perimeter
  distance = 0
  for i in range(n):
    distance = distance + step
    t.forward(step)
    t.right(360.0/n)
    
  return distance

# If the number of polygon's sides is increased towards infinity, the
# polygon can be thought to trace the circle exactly eventually. The
# total distance along the infinite-sided polygon (that is, the true
# circumference of the circle) will be the value computed on the next
# line. (Proving this requires some rather advanced mathematical
# tools.)

true_circumference = 2 * pi * r

##### EXERCISES #####
# polygon(3) draws a triangle. Press run and see what happens!
#
# Try increasing the number of of polygon's sides (the number in the
# parenthesis) and observe how the polygon matches the circle better
# and better.

distance = polygon(3)

print "Polygon's perimeter: " + str(distance)
print "Circle's true circumference: " + str(true_circumference)
print "Difference: " + str(true_circumference - distance)

# How many sides the polygon must at least have so that the difference
# to the correct circumference (see the last print command) is less
# than 1 % of the circle's true circumference?

# How many sides are required so that you don't see any difference
# between the polygon and the circle on the screen?
