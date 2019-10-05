##### INFO #####

# Tiedoston alussa on paljon koodia, jolla luodaan pelialue.
# Skrollaa alas päästäksesi tehtäviin

import turtle2
import random
import time


# Luo listan numeroita a:sta b:hen tasavälein
def lineaarisetValit(a, b, valinPituus):
  xs = []
  x = a
  while x <= b:
    xs.append(x)
    x = x + valinPituus
  return xs


# Luo n satunnaista esteittä kilpikonnalle.
# Esteet ovat horisontaalisia suorakulmioita,
# jotka luodaan parametrien vasenReuna, oikeaReuna, ylaReuna, alaReuna sisälle
def luoEsteet(n, vasenReuna, oikeaReuna, ylaReuna, alaReuna):
  korkeus = 20
  minLeveys = round(0.1 * (oikeaReuna - vasenReuna))
  maxLeveys = round(0.8 * (oikeaReuna - vasenReuna))

  vaihtoehdot = lineaarisetValit(alaReuna, ylaReuna, 2 * korkeus)
  random.shuffle(vaihtoehdot)
  vaihtoehdot = sorted(vaihtoehdot[:n])

  esteet = []
  for y in vaihtoehdot:
    x1 = random.randint(vasenReuna - maxLeveys + minLeveys, oikeaReuna - minLeveys)
    x = max(x1, vasenReuna)
    leveys = random.randint(minLeveys, maxLeveys)
    leveys = min(leveys, oikeaReuna - x)

    esteet.append((x, y, leveys, korkeus))

  return esteet


# Luo pelialuetta reunustavien suorakulmioiden parametrit
def ulkoReunat(vasen, oikea, yla, ala):
  w = 20
  return [
    (vasen - w, ala - w, w, yla - ala + w),
    (vasen, ala - w, oikea - vasen, w),
    (oikea, ala - w, w, yla - ala + w)
  ]


# Piirtää suorakulmion pisteestä (x, y) alkaen. Suorakulmiosta tulee
# muuttuja "leveys" levyinen ja "korkeus" korkuinen.
# Piirtämiseen käytetään turtle oliota "kilppari"
def piirraSuorakulmio(kilppari, x, y, leveys, korkeus):
  kilppari.penup()
  kilppari.setheading(0)
  kilppari.goto(x, y)
  kilppari.pendown()
  kilppari.begin_fill()
  kilppari.forward(leveys)
  kilppari.left(90)
  kilppari.forward(korkeus)
  kilppari.left(90)
  kilppari.forward(leveys)
  kilppari.end_fill()
  kilppari.penup()


# Piirrä suorakulmiot.
# suorakulmiot on lista muuttujia (x, y, leveys, korkeus)
def piirraSuorakulmiot(suorakulmiot):
  t = turtle2.Turtle()
  t.speed("fastest")
  t.color("red")
  t.hideturtle()
  for rect in suorakulmiot:
    piirraSuorakulmio(t, rect[0], rect[1], rect[2], rect[3])


def piirraMaaliviiva(x1, x2, y):
  t = turtle2.Turtle()
  t.hideturtle()
  t.speed("fastest")
  t.color("blue")
  t.pensize(3)
  t.penup()
  t.goto(x1, y)
  t.pendown()
  t.goto(x2, y)


# Palauttaa True, jos koordinaatti (x, y) on suorakulmion sisässä
def ollankoSuorakulmionSisalla(x, y, suorakulmio):
  return (x >= suorakulmio[0] and x < suorakulmio[0] + suorakulmio[2] and
      y >= suorakulmio[1] and y < suorakulmio[1] + suorakulmio[3])


# Palauttaa True, jos (x, y) on minkään suorakulmioLista:n
# suorakulmion sisällä
def ollaankoMinkaanSuorakulmionSisalla(x, y, suorakulmioLista):
  for suorakulmio in suorakulmioLista:
    if ollankoSuorakulmionSisalla(x, y, suorakulmio):
      return True
  return False


# Alla oleva funktio liikutta kilpparia.
# Funktio valitsee kilpparille suunnan ja siirtää sitä hieman eteenpäin.
# Kun funtiota kutsutaan toistuvasti, kilppari liikkuu satunnaisesti esteradalla
def siirryAskel(kilppari, esteet):
  x = kilppari.xcor()
  y = kilppari.ycor()

  if ollaankoMinkaanSuorakulmionSisalla(x, y, esteet):
    kilppari.right(180)
  else:
    kilppari.right(random.randint(-30, 30))

  kilppari.forward(10)


# Luodaan esteitä satunnaisiin paikkoihin käyttämällä yllä olevia funktioita
screen = turtle2.Screen()
oikea = min(250, screen.window_width() / 2 - 5)
vasen = -oikea
yla = min(270, screen.window_height() / 2 - 5)
ala = -yla

esteet = (ulkoReunat(vasen, oikea, yla, ala) +
      luoEsteet(4, vasen, oikea, yla - 20, ala + 60))

# Piirrä esteet
turtle2.pauseDrawing()
piirraSuorakulmiot(esteet)
piirraMaaliviiva(vasen, oikea, yla)
turtle2.unpauseDrawing()

# Create the turtle
kilpppari = turtle2.Turtle()
kilpppari.speed("fastest")
kilpppari.penup()
kilpppari.goto((vasen + oikea) / 2, ala + 20)
kilpppari.setheading(90)
kilpppari.pendown()

# Tämä looppi liikuttaa kilpparia, kunnes se saavuttaa maaliviivan
aloitusaika = time.time()
while kilpppari.ycor() < yla:
  siirryAskel(kilpppari, esteet)
lopetusaika = time.time()

print "Kilppari saavutti maaliviivan %d sekunnissa!" % round(lopetusaika - aloitusaika)


##### TEHTÄVÄ 1 #####

# Aja koodi 'Run' napista ja katso mitä tapahtuu.
# Kuinka kauan kilpikonnalla kestää päästä maaliin?
#
# Yritä nyt ymmärtää miten siirryAskel -funktio hallitsee kilpikonnan liikkeitä
#
# Kun ajat koodin uudelleen, uudet esteet luodaan uusiin paikkoihin


##### TEHTÄVÄ 2 #####

# Kilpparilla voi kestää varsin kauan päästä maaliin, koska sen
# liikkeet ovat satunnaisia.
#
# Muokkaa siirryAskel -funktiota niin että kilpikonna valitsee välillä
# satunnaisen suunnan ja välillä liikkuu ylöspäin
# Saat kilpparin kääntymään ylöspäin komennolla:
#
# kilppari.setheading(90)
#
# Saavuttaako kilppari maaliviivan nyt nopeammin?

##### TEHTÄVÄ 3 #####

# Keksi nyt erilaisia taktiikoita kilpparin liikkumiselle ja toteuta ne
# siirryAskel -funktiotioon
#
# Esimerkiksi: muuta kilpparin suuntaa vain, jos se osuu esteeseen ja
# liiku muuten suoraan.
#
# Miten saat kilpparin nopeiten maaliin?

#### EXTRA TEHTÄVÄ #####

# Muuta esteiden muotoja muokkaamalla luoEsteet -funktiota.
# Kokeile esim. pystsuunnassa olevia suorakulmioita.
#
# Voit myös kokeilla ympyröitä, mutta silloin pitää myös muokata
# piirtämisen ja törmäyksen havaitsevaa funktioita
# piirraSuorakulmio ja ollankoSuorakulmionSisalla
