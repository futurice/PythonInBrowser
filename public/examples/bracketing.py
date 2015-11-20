# bracketing.py
import turtle

# Here we define a prepare functions that we use to prepare our exercise.
def prepare():
  wall = turtle.Turtle()
  wall.penup()
  wall.speed(0)
  wall.goto(0, -500)
  wall.left(90)
  wall.pendown()
  wall.forward(1000)

# Here we actually call the function so that what it has inside will actually happen
# We learn these things later so don't worry if you don't understand everything
prepare()

# Exercise:
# How long can the turtle travel until it hits the wall?
# Modify the angle. It controls how much the turtle turns.

angle = 180

t = turtle.Turtle()
t.forward(70)
t.circle(80, angle)

print "X coordinate = ", t.xcor()
print "The turtle is on the left side of the wall?", t.xcor() < 0
