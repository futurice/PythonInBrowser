##### FILE #####
# dots.py
# Conneting dots

import coordinates
import turtle

coordinates.prepareCoordinates()
coordinates.drawDots()
t = turtle.Turtle()

##### EXERCISE #####
# 1. Use goto penup and pendown to connect all the dots and form a fish
# (0, 50) (0, 100) (100, 0) (100, 150) (50, 75)
# (-150, 20) (-200, 50) (-200, 125)
# (-250, 75) (-250, 35)

t.penup()
t.goto(100, 0)
t.pendown()
t.goto(50, 75)
t.goto(100, 150)
t.goto(0, 100)
t.goto(-200, 125)
t.goto(-250, 75)
t.goto(-200, 50)
t.goto(-250, 35)
t.goto(-150, 20)
t.goto(0, 50)
t.goto(100, 0)

# 2. Draw an eye to the fish with a dot, you can use it like this
# t.dot(5)
t.penup()
t.goto(-200, 85)
t.dot(5)
t.home()

