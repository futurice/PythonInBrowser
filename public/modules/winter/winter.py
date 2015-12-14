import turtle
import random

# This function will draw one snowflake that has 6 brances like *
def snowflake(t, lenght):
  for i  in range(0, 3):
    snowflakeBranch(t, lenght)
    t.right(60)

# This function will draw two branches of snowflake that are on the same line
def snowflakeBranch(t, lenght):
  for i  in range(0, 2):
    t.pendown()
    t.forward(lenght)
    t.backward(lenght/3.0)
    t.left(30)
    t.forward(lenght/3.0)
    t.backward(lenght/3.0)
    t.right(60)
    t.forward(lenght/3.0)
    t.backward(lenght/3.0)
    t.right(150)
    t.forward(2 * lenght/3.0)

# This function creates turtle and draws snowflakes 'max' times
# The size of the snowflake is random value between 10-30
# The position of snowflake is (x, y) where x and y vary from -300 to 300
def letThereBeSnow(max):
  screen = turtle.Screen()
  screen.bgcolor("#deeff5")
  turt = turtle.Turtle()
  turt.color("lightblue")
  turt.speed("fastest")
  for s in range(0, max):
    turt.penup()
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    size = random.uniform(10, 30)
    turt.goto(x, y)
    snowflake(turt, size)

