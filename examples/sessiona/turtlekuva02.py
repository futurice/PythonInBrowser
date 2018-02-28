## Hypnotic squares

import turtle
taylor = turtle.Turtle()
taylor.speed(0)

c = 0
x = 0


while x < 500:
    idx = int(c)
    taylor.forward(x)
    taylor.right(98)
    x = x + 1
    c = c + 0.3
