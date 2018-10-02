# Etsi reitti esteiden läpi

import turtle

##### INFO #####

# Tämä osa koodista piirtää esteet ja maalin

seina = turtle.Turtle()
seina.hideturtle()
seina.speed(0)
seina.width(3)
seina.color('dark green')
for x in [-180, -20, 140]:
  seina.penup()
  seina.goto(x, -160)
  seina.pendown()
  seina.goto(x, 120)
  seina.penup()
  
  x2 = x + 80
  seina.penup()
  seina.goto(x2, -500)
  seina.pendown()
  seina.goto(x2, -130)
  seina.penup()
  seina.goto(x2, 100)
  seina.pendown()
  seina.goto(x2, 500)

seina.penup()
seina.goto(-500, 0)
seina.pendown()
seina.goto(220, 0)
  
seina.penup()
seina.goto(-250, -70)
seina.dot(20, 'red')

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
