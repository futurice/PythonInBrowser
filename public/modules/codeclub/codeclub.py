import turtle
scale = 0.6
def rt(angle, t, factor):
    t.circle(-scale*factor, angle)

def lt(angle, t, factor):
    t.circle(scale*factor, angle)

def rightTurn(angle, t):
    rt(angle, t, 120)

def leftTurn(angle, t):
    lt(angle, t, 120)

def rightTurnEasy(angle, t):
    rt(angle, t, 240)

def leftTurnEasy(angle, t):
    lt(angle, t, 240)

def rightTurnHard(angle, t):
    rt(angle, t, 60)

def leftTurnHard(angle, t):
    lt(angle, t, 60)

def fd(lenght, t):
    t.forward(lenght * scale)


def drawCircleArena(t):
    t.penup()
    t.speed(0)
    t.goto(0, -200)
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

    t.color("black")
    t.setheading(0)
    t.goto(0, -250)
    t.speed(6)
    t.pendown()


def drawArena(t):
    t.penup()
    t.speed(0)
    t.goto(-50, 0)
    t.right(90)
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
    fd(283, t)
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
    t.color("black")
    t.setheading(0)
    t.goto(-50, -95)
    t.speed(6)
    t.pendown()


def drawArena2(t, scale=1.0):
    t.speed(0)
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
    t.speed(6)
    t.pendown()


def drawArena3(t, scale=1.0):
    t.speed(0)
    t.penup()
    t.goto(-scale*280, scale*50)
    t.setheading(80)
    t.pendown()
    
    t.forward(scale*140)
    t.circle(-scale*30, 90)
    t.forward(scale*240)
    t.circle(scale*10, 110)
    t.forward(scale*50)
    t.circle(-scale*40, 80)
    t.forward(scale*70)
    t.circle(-scale*40, 110)
    t.forward(scale*80)
    t.circle(scale*5, 180)
    t.forward(scale*40)
    t.circle(-scale*30, 90)
    t.forward(scale*70)
    t.circle(-scale*40, 110)
    t.forward(scale*130)
    t.circle(-scale*160, 80)
    t.forward(scale*210)
    t.circle(scale*30, 90)
    t.forward(scale*260)
    t.circle(-scale*60, 90)
    t.forward(scale*16)
    t.circle(-scale*60, 90)
    t.forward(scale*303)
    
    
    t.penup()
    t.goto(-scale*220, scale*20)
    t.pendown()
    t.forward(scale*130)
    t.circle(-scale*10, 90)
    t.forward(scale*220)
    t.circle(scale*40, 110)
    t.forward(scale*70)
    t.circle(-scale*10, 80)
    t.forward(scale*40)
    t.circle(-scale*10, 110)
    t.forward(scale*80)
    t.circle(scale*40, 90)
    t.forward(scale*15)
    t.circle(scale*40, 90)
    t.forward(scale*30)
    t.circle(-scale*10, 90)
    t.forward(scale*30)
    t.circle(-scale*10, 110)
    t.forward(scale*80)
    t.circle(-scale*140, 80)
    t.forward(scale*240)
    t.circle(scale*40, 90)
    t.forward(scale*300)
    t.circle(-scale*9, 180)
    t.forward(scale*285)
    
    t.color('red')
    t.left(90)
    t.forward(scale*64)
    
    t.penup()
    t.right(180)
    t.forward(scale*32)
    t.left(90)
    t.color('black')
    t.speed(6)
    t.pendown()
