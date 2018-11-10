# Opi piirtämään rajojen sisällä.

##### INFO #####
import turtle
import random

# Kutsutaan kilpikonna ja annetaan sille nopeus
t = turtle.Turtle()
t.speed("fastest")
t.color("black")

# Lasketaan piirtoalueen koko
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()
maxLeveys = width / 2
minLeveys = -maxLeveys
maxKorkeus = height / 2
minKorkeus = -maxKorkeus

# Funktio, joka liikuttaa kilpikonnaa
def teeLiike():
  # Säilötään kilpikonnan sijainti muuttujissa x ja y
  x = t.xcor()
  y = t.ycor()
  # Seuraava ehtolauseke tarkistaa että kilpikonna pysyy piirtoalueen sisällä
  if (x < maxLeveys) and (x > minLeveys) and (y < maxKorkeus) and (y > minKorkeus):
    # jos kilpikonna on piirtoalueen sisällä,
    # siirtyy se 10 askelta eteenpäin
    t.forward(10)
  else:
    # jos kilpikonna ei ole piirtoalueen sisässä,
    # kääntyy se 120 astetta oikealle..
    t.right(120)
    # ..ja siirtyy 10 askelta eteenpäin
    t.forward(10)

##### TEHTÄVÄ #####

# Klikkaa 'Run' ja katso mitä tapahtuu.

# Tämä rivi printaa laskemamme piirtoalueen mitat
print(maxLeveys, minLeveys, maxKorkeus, minKorkeus)

# Tässä kutsumme teeLiike() funktiota toistuvasti
while True:
  teeLiike()

# Aikaisemmissa tehtävissä olemme antaneet kilpikonnalle vain
# selkeästi määriteltyjä käskyjä.

# Miksi voisi olla hyödyllistä määritellä kilpikonnan toimita ehtolauseilla if ja else?
# Kokeile nyt muuttaa selainikkunasi kokoa ja klikkaa 'Run' uudelleen.

# Huomaatko että kilpikonna sopeutui uusiin olosuhteisiin?

# Kun annamme kilpikonnalle ehtoja suorien käskyjen sijaan,
# pystyy kilpikonna liikkumaan uusissa olosuhteissa.
# Tämä osoittautuu hyödylliseksi myöhemmin.
