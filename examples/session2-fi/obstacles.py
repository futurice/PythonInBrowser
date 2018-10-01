# Etsi reitti esteiden läpi

import turtle

##### INFO #####

# Tämä osa koodista piirtää esteet ja maalin

wall = turtle.Turtle()
wall.hideturtle()
wall.speed(0)
wall.width(3)
wall.color('dark green')
for x in [-180, -20, 140]:
  wall.penup()
  wall.goto(x, -160)
  wall.pendown()
  wall.goto(x, 120)
  wall.penup()
  
  x2 = x + 80
  wall.penup()
  wall.goto(x2, -500)
  wall.pendown()
  wall.goto(x2, -130)
  wall.penup()
  wall.goto(x2, 100)
  wall.pendown()
  wall.goto(x2, 500)

wall.penup()
wall.goto(-500, 0)
wall.pendown()
wall.goto(220, 0)
  
wall.penup()
wall.goto(-250, -70)
wall.dot(20, 'red')

tess = turtle.Turtle()
tess.speed(0)
tess.penup()
tess.goto(-260, 40)
tess.pendown()
tess.speed(6)

##### TEHTÄVÄ #####

# Ohjaa Tess-kilpikonna punaiselle pisteelle. Varo seiniä!
#
# Jatka seuraavaa koodia. Voit laittaa Tess-kilpikonnan
# toistamaan koodinpätkän useampaan kertaan muuttamalla
# range(1) komennossa 1:sen joksikin muuksi numeroksi.

tess.left(90)
tess.forward(30)
tess.right(135)

for i in range(1):
  tess.left(90)
  tess.forward(114)
  tess.right(90)
  tess.forward(114)
