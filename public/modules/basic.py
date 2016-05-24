import turtle2

def drawAxis(t, minW, minH):
  t.goto(minW, minH)
  t.pendown()
  t.forward(1200)
  t.penup()


def drawTicksX(t, min):
  for x in range(0, 30):
    t.goto(min + 50 * x, 0)
    t.pendown()
    t.forward(5)
    t.penup()


def drawTicksY(t, min):
  for x in range(0, 30):
    t.goto(0, min + 50 * x)
    t.pendown()
    t.forward(5)
    t.penup()


def drawXnumbers(t, minValue):
  t.penup()
  t.goto(minValue, 0)

  for x in range(0, 30):
    if x == 0:
      t.goto(minValue + 48 * x, 10)
    else:
      t.goto(minValue + 50 * x, 10)
    t.write(minValue + 50 * x)


def drawYnumbers(t, minValue):
  t.penup()
  t.goto(0, minValue)

  for x in range(0, 30):
    if x == 0:
      t.goto(10, minValue + 48 * x)
    elif minValue + 50 * x == 0:
      continue
    else:
      t.goto(10, minValue + 50 * x)
    t.write(minValue + 50 * x)


def drawDots():
  joe = turtle2.Turtle()
  size = 4
  joe.penup()
  joe.color("blue")
  joe.goto(0, 50)
  joe.dot(size)
  joe.goto(0, 100)
  joe.dot(size)
  joe.goto(100, 0)
  joe.dot(size)
  joe.goto(100, 150)
  joe.dot(size)
  joe.goto(50, 75)
  joe.dot(size)
  joe.goto(-150, 20)
  joe.dot(size)
  joe.goto(-250, 35)
  joe.dot(size)
  joe.goto(-200, 50)
  joe.dot(size)
  joe.goto(-250, 75)
  joe.dot(size)
  joe.goto(-200, 125)
  joe.dot(size)
  joe.penup()
  joe.goto(600, 600)


def prepareCoordinates():
  turtle2.pauseDrawing()
  t = turtle2.Turtle()
  t.color("#545454")
  t.hideturtle()
  t.speed(0)
  t.penup()
  drawAxis(t, -600, 0)
  t.right(270)
  drawAxis(t, 0, -600)
  drawTicksX(t, -600)
  t.right(270)
  drawTicksY(t, -600)
  drawXnumbers(t, -600)
  drawYnumbers(t, -600)
  turtle2.unpauseDrawing()

