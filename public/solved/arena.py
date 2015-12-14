# File
# arena.py

import codeclub
import turtle
codeclub.drawArena()

t = turtle.Turtle()
t.penup()
t.goto(-40, -90)
t.pendown()
codeclub.fd(350, t)
codeclub.leftTurnEasy(90, t)
codeclub.leftTurnHard(90, t)
codeclub.fd(200, t)
codeclub.leftTurnHard(45, t)
codeclub.rightTurn(110, t)
codeclub.leftTurnHard(65, t)
codeclub.fd(350, t)
codeclub.leftTurn(90, t)
codeclub.leftTurnEasy(90, t)
codeclub.fd(300, t)

