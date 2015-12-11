import turtle
scale = 0.6
def rt(angle, t, factor):
    for i in range(0, angle):
        t.forward(factor * scale)
        t.right(1)

def lt(angle, t, factor):
    for i in range(0, angle):
        t.forward(factor * scale)
        t.left(1)

def rightTurn(angle, t):
    rt(angle, t, 2)

def leftTurn(angle, t):
    lt(angle, t, 2)

def rightTurnEasy(angle, t):
    rt(angle, t, 4)

def leftTurnEasy(angle, t):
    lt(angle, t, 4)

def rightTurnHard(angle, t):
    rt(angle, t, 1)

def leftTurnHard(angle, t):
    lt(angle, t, 1)

def fd(lenght, t):
    t.forward(lenght * scale)

def drawCircleArena():
    t = turtle.Turtle()
    t.penup()
    t.goto(0, -200)
    t.speed(0)
    t.pendown()
    t.circle(200)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.circle(300)
    t.left(90)
    t.color("red")
    t.forward(100)
    t.penup()
    t.goto(600, 600)


def drawArena():
    t = turtle.Turtle()
    t.penup()
    t.goto(-50, 0)
    t.right(90)
    t.speed(0)
    t.penup()
    fd(100, t)
    t.left(90)
    t.pendown()
    fd(400, t)
    leftTurn(90, t)
    leftTurn(90, t)
    leftTurn(45, t)
    fd(100, t)
    rightTurn(90, t)
    fd(100, t)
    leftTurn(45, t)
    fd(200, t)
    leftTurn(180, t)
    fd(270, t)
    t.penup()
    t.right(90)
    fd(110, t)
    t.left(90)
    t.pendown()
    fd(400, t)
    leftTurnEasy(225, t)
    fd(50, t)
    rightTurnHard(90, t)
    fd(50, t)
    leftTurnEasy(45, t)
    fd(200, t)
    leftTurnEasy(90, t)
    fd(2, t)
    leftTurnEasy(90, t)
    fd(300, t)
    t.left(90)
    t.color("red")
    fd(110, t)
    t.penup()
    t.goto(600, 600)

