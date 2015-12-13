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


def drawArena2(scale=1.0):
    t = turtle.Turtle()
    t.speed('fastest')
    t.penup()
    t.goto(0, scale*250)
    t.pendown()
    t.forward(scale*100)
    t.circle(-scale*200, 90)
    t.forward(scale*60)
    t.circle(-scale*200, 70)
    t.circle(-scale*140, 70)
    t.forward(scale*200)
    t.circle(scale*30, 110)
    t.forward(scale*160)
    t.circle(-scale*60, 160)
    t.forward(scale*335)
    t.circle(-scale*30, 80)
    t.forward(scale*268)
    t.penup()
    
    t.goto(0, scale*170)
    t.pendown()
    t.forward(scale*100)
    t.circle(-scale*120, 90)
    t.forward(scale*60)
    t.circle(-scale*120, 70)
    t.circle(-scale*70, 70)
    t.forward(scale*210)
    t.circle(scale*85, 110)
    t.forward(scale*120)
    t.circle(-scale*5, 160)
    t.forward(scale*210)
    t.circle(-scale*20, 80)
    t.forward(scale*223)
    
    t.color('red')
    t.left(90)
    t.forward(scale*80)
    
    t.color('black')
    t.penup()
    t.setheading(0)
    t.goto(0, scale*210)
    t.pendown()
