# Colorful honeycombs

import turtle
from random import randint


taylor = turtle.Turtle()
taylor.speed(100)
taylor.color(255)


def move(length, angle):
    taylor.right(angle)
    taylor.forward(length)


def hex():
    """Draw one hex at current location"""
    taylor.pendown()
    taylor.color( randint(0,255),randint(0,255),randint(0,255) )
    taylor.begin_fill()
    for i in range(6):
        move(size,-60)
    taylor.end_fill()
    taylor.penup()


# start
size = 20
circles = 20
taylor.penup()

for circle in range(circles):
    if circle == 0:
            hex()
            move(size, -60)
            move(size, -60)
            move(size, -60)
            move(0, 180)
    for i in range(6):
            move(0, 60)
            for j in range(circle + 1):
                    hex()
                    move(size, -60)
                    move(size, 60)
            move(-size, 0)
    move(-size, 60)
    move(size, -120)
    move(0, 60)
