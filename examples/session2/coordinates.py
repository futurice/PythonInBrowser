# Drawing points to coordinate system

import coordinates
import turtle

# Prepare coordinates and turtle
coordinates.prepareCoordinates()
t = turtle.Turtle()

##### INFO #####
# Next we'll learn few new turtle commands.
#
# Penup:
# t.penup(), it means we can lift the pen up and just move turtle a round.
#
# Pendown:
# t.pendown(), put pen back down and start drawing
#
# Goto:
# t.goto(10, 20), moves our turlte from the current position to position (10, 20)
#
# Dot:
# t.dot(2), draw small dot on the current position
#
# Home:
# t.home(), move back to position (0,0)

##### EXERCISE #####
# 1. Try these commands freely
t.forward(100)
t.right(30)
t.penup()
t.forward(200)
t.dot(5)
t.pendown()
t.right(90)
t.forward(50)
t.home()


# 2. Run this code and see what happens.
# Fix it by adding t.pendown() and t.penup() between lines
# as many times as needed so that you'd have only blue square in the canvas

#t.color("blue")
#t.goto(-150, 0)
#t.goto(0, 150)
#t.goto(0, 0)
#t.goto(150, 0)
#t.goto(0, -150)
#t.goto(0, 0)
#t.goto(-150, 0)
#t.goto(0, -150)
#t.goto(0, 0)
#t.goto(150, 0)
#t.goto(0, 150)
#t.goto(0, 0)


