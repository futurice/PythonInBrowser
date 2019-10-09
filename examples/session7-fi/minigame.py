# Kilppari liikkuu kuutioiden ympärillä

##### INFO #####
import turtle2
import random

# Määritellään kilppari ja sen nopeus
t = turtle2.Turtle()
t.speed("fastest")
t.color("black")

# Lasketaan piirtoalueen koko
screen = turtle2.Screen()
screen.bgcolor("blue")
leveys = screen.window_width()
korkeus = screen.window_height()
maxLeveys = leveys / 2
minLeveys = -maxLeveys
maxKorkeus = korkeus / 2
minKorkeus = -maxKorkeus


def sekoita_varit(color1, color2, weight1=1.0, weight2=1.0):
  u = weight1 / (weight1 + weight2)
  v = weight2 / (weight1 + weight2)
  return (u * color1[0] + v * color2[0],
          u * color1[1] + v * color2[1],
          u * color1[2] + v * color2[2])


def piirra_kuutio(t, x, y, color=(255, 0, 0), size=50):
  turtle2.pauseDrawing()
  t.speed("fastest")
  t.hideturtle()
  t.penup()
  t.goto(x, y)
  t.setheading(90)
  t.pendown()

  # Oikea puoli
  t.fillcolor(sekoita_varit(color, (0, 0, 0)))
  t.begin_fill()
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.end_fill()
  
  # Vasen puoli
  t.fillcolor(sekoita_varit(color, (0, 0, 0), weight1=3.0))
  t.begin_fill()
  t.right(60)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.end_fill()

  # Yläpuoli
  t.fillcolor(color)
  t.begin_fill()
  t.right(180)
  t.forward(size)
  t.right(120)
  t.forward(size)
  t.right(60)
  t.forward(size)
  t.end_fill()

  turtle2.unpauseDrawing()


def luo_esteet(n):
  t = turtle2.Turtle()
  t.speed("fastest")
  t.color("red")

  esteLista = []
  for i in range(n):
    x = random.randint(-maxLeveys, maxLeveys)
    y = random.randint(-maxKorkeus, maxKorkeus)
    w = random.randint(10, 300)
    h = random.randint(10, 300)

    piirra_kuutio(t, x, y)
    esteLista.append((x, y, w, h))

  t.hideturtle()
  return esteLista


def ollanko_kuution_sisalla(x, y, kuutio):
  return (x >= kuutio[0] and x < kuutio[0] + kuutio[2] and
          y >= kuutio[1] and y < kuutio[1] + kuutio[3])


def ollanko_minkaan_kuution_sisalla(x, y, kuutioLista):
  for kuutio in kuutioLista:
    if ollanko_kuution_sisalla(x, y, kuutio):
      return True
  return False


def ollaanko_nayton_ulkopuolella(x, y):
  return x < minLeveys or y < minKorkeus or x >= maxLeveys or y >= maxKorkeus


def tee_liike():
  kuutios = luo_esteet(10)

  while True:
    x = t.xcor()
    y = t.ycor()

    if ollaanko_nayton_ulkopuolella(x, y):
      t.right(180)
    elif ollanko_minkaan_kuution_sisalla(x, y, kuutios):
      t.right(180)
    else:
      t.right(random.randint(-30, 30))

    t.forward(10)

# Seuraava aloittaa animaation
t.penup()
tee_liike()

##### TEHTÄVÄ #####

# Muistatko estetehtävän? Tämä on uusi versio siitä.
# Suorakulmioiden sijaan kilppari väistelee nyt kuutioita.
# Tehtävää ei kuitenkaan ole muokattu tarpeeksi!
# Huomaa että kuutioilla ja suorakulmioilla on erilaiset rajat
# Korjaa koodi alla olevien ohjeiden mukaisesti

# 1. Korjaa rajat niin että kilppari ei pääse kuutioiden sisään

# 2. Muuta taustaväri haluamaksesi

# 3. Valitse kuutioiden väri satunnaisesti

# 4. Pystytkö lisäämään maaliviivan, kuten tunnin 6 tehtävässä 1
