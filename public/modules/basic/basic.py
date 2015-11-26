import turtle

t = turtle.Turtle()

def drawAxis(minW, minH):
  t.goto(minW, minH)
  t.pendown()
  t.forward(1200)
  t.penup()


def drawTicksX(min):
  for x in range(0, 30):
    t.goto(min + 50 * x, 0)
    t.pendown()
    t.forward(5)
    t.penup()


def drawTicksY(min):
  for x in range(0, 30):
    t.goto(0, min + 50 * x)
    t.pendown()
    t.forward(5)
    t.penup()

def drawXnumbers(minValue):
  t.penup()
  t.goto(minValue, 0)

  for x in range(0, 30):
    if x == 0:
      t.goto(minValue + 48 * x, 10)
    else:
      t.goto(minValue + 50 * x, 10)
    t.write(minValue + 50 * x)

def drawYnumbers(minValue):
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


def prepareCoordinates():
  t.speed(0)
  t.penup()
  drawAxis(-600, 0)
  t.right(270)
  drawAxis(0, -600)
  drawTicksX(-600)
  t.right(270)
  drawTicksY(-600)
  drawXnumbers(-600)
  drawYnumbers(-600)

