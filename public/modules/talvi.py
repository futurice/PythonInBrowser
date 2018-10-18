import turtle
import random

# Tämä funtio piirtää yhden lumihiutaleen, jolla on 6 sakaraa, kuten *
def lumihiutale(t, lenght):
  for i  in range(0, 3):
    lumihiutaleenSakara(t, lenght)
    t.right(60)

# Seuraava funktio piirtää lumiutaleen kaksi sakaraa, jotka ovat toisiaan vasten
def lumihiutaleenSakara(t, lenght):
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

# Seuraava funktio luo kilpikonnan ja piirtää lumihiutaleita 'max' kertaa
# Lumihiutaleen koko on satunnainen arvo väliltä 10-30
# Lumihiutaleen koordinaatit (x, y) vaihtelevat välillä -300 ja 300
def tulkoonLumi(max):
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
    lumihiutale(turt, size)

