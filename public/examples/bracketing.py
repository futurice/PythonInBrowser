# bracketing.py
import turtle

# Initialization:
wall = turtle.Turtle()
wall.penup()
wall.speed(0)
wall.goto(0, -500)
wall.left(90)
wall.pendown()
wall.forward(1000)

# Exercise:
# How long can the turtle travel until it hits the wall?
# Modify the angle. It controls how much the turtle turns.
# Test different values for the angle and try to find the
# exact value when the turtle hits the wall.

angle = 180.0

t = turtle.Turtle()
t.forward(70)
t.circle(80, angle)

print "X coordinate = ", t.xcor()
print "The turtle is on the left side of the wall?", t.xcor() < 0
