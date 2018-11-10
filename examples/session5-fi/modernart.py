# Modernia taidetta
# Opi lukemaan koodia, ymmärtämään funktioita ja satunnaisuutta
import turtle
import random

##### TEHTÄVÄ #####

##### TEHTÄVÄ 1 #####
# Lue läpi seuraavat funktiot ja yritä ymmärtää mitä ne tekevät.
# Älä murehdi jos et heti ymmärrä aivan kaikkea.

t = turtle.Turtle()

rajaMax = 180.0
rajaMin = -180.0

# Tämä funktio piirtää kaksi neliötä, jotka muodostavat taideteoksen reunat
def esivalmisteleModerniTaideteos():
  t.speed(0)
  t.penup()
  t.goto(-220, -220)
  t.pendown()
  nelio(440)
  t.penup()
  t.goto(-180, -180)
  t.pendown()
  nelio(360)
  t.penup()
  t.goto(0,0)
  t.right(35)
  t.pendown()
  t.color("green")
  t.speed(6)

# Tämä funktio piirtää neliön
def nelio(sivu):
  for i in range(0, 4):
    t.forward(sivu)
    t.left(90)

# Tätä funktiota kutsutaan jos kilpikonna joutuu
# neliön rajojen ulkopuolelle
def tormays():
  x = t.xcor() #  kilpikonnan x koordinaatti
  y = t.ycor() #  kilpikonnan y koordinaatti

  # Tarkistetaan onko kilpikonna 15 askelta kauempana sisäneliöstä
  xYliReunojen = (x - rajaMax > 15) or (rajaMin - x > 15)
  yYliReunojen = (y - rajaMax > 15) or (rajaMin - y > 15)
  if xYliReunojen or yYliReunojen:
    # jos ehto täyttyy, kutsutaan funktiota 'isoTormays'
    isoTormays()
  else:
    # muussa tapauksessa kutsutaan funktiota 'pieniTormays'
    pieniTormays()

# Funktio, jolla hoidetaan pienet törmäykset
def pieniTormays():
  kulma = random.randint(20, 70) # satunnainen luku väliltä 20-70
  t.color("blue")
  t.right(kulma)
  t.forward(10)

# Funktio, jolla hoidetaan isot törmäykset
def isoTormays():
  t.color("red")
  t.right(175)
  t.forward(30)

# Funktio, joka hoitaa kilpikonnan liikkumisen
def teeLiike():
  x = t.xcor()
  y = t.ycor()
  # Tarkistetaan onko kilpikonna rajojen sisällä
  xRajojenSisalla = (x <= rajaMax) and (x >= rajaMin)
  yRajojenSisalla = (y <= rajaMax) and (y >= rajaMin)
  if xRajojenSisalla and yRajojenSisalla:
    t.color("green")
    t.forward(10)
  else:
    # Jos kilpikonna on rajojen ulkopuolella, kutsutaan funktiota 'tormays'
    tormays()

# Tämä on ensimmäinen funktiokutsu, jonka ohjelma tekee
esivalmisteleModerniTaideteos()

# Kutsutaan seuraavaksi teeLiike() toistuvasti
while True:
  teeLiike()

##### TEHTÄVÄ 2 #####

# Saatat nyt huomata, että 'esivalmisteleModerniTaideteos' ainoa funktio,
# jota kutsutaan muiden funktioiden ulkopuolella.

# Lue nyt koodi uudelleen aloittaen 'esivalmisteleModerniTaideteos' funktion
# kutsusta ja katso mitä funktioita se puolestaan kutsuu.

# Vikkejä:
#   - Voit hahmotella kutsujen järjestystä kynällä ja paperilla
#   - Kiinnitä huomiota siihen mitä väriä jokainen funktio käyttää ja
#     vertaa sitä kilpikonnaan toimintaan piirtoalueella
#   - Voit myös lisätä printtauksia funktioiden sisälle niin että näet
#     missä kohtaa koodia olet samalla kun kilpikonna piirtää
