import turtle

def pauseDrawing():
  turtle.tracer(10000)


def unpauseDrawing():
  turtle.update()
  turtle.tracer(1)
