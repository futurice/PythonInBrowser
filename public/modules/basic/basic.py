import turtle

t = turtle.Turtle()

def drawAxis(minW, minH):
  t.goto(minW, minH)
  t.pendown()
  t.forward(1200)
  t.penup()


def drawTicksX(min):
  for x in range(0, 12):
    t.goto(min + 100 * x, 0)
    t.pendown()
    t.forward(10)
    t.penup()


def drawTicksY(min):
  for x in range(0, 12):
    t.goto(0, min + 100 * x)
    t.pendown()
    t.forward(10)
    t.penup()


def prepareCoordinates():
  # Speed drawing
  t.speed(0)
  t.penup()
  # Draw axis
  drawAxis(-600, 0)
  t.right(270)
  drawAxis(0, -600)
  drawTicksX(-600)
  t.right(270)
  drawTicksY(-600)

