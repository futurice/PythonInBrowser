# Liikuta kilpikonna esteiden ohi

##### INFO #####
import turtle
import random
# Alussa on koodia, joka alustaa esteradan. Skrollaa alas tehtäviin

# Luodaan kilpikonna ja annetaan sille nopeus ja väri
t = turtle.Turtle()
t.speed("fastest")
t.color("black")

# Lasketaan piirtoalueen koko
screen = turtle.Screen()
leveys = screen.window_leveys()
korkeus = screen.window_korkeus()
maxleveys = leveys / 2
minleveys = -maxleveys
maxkorkeus = korkeus / 2
minkorkeus = -maxkorkeus

def piirraSuorakulmio(t, x, y, w, h):
  t.penup()
  t.setheading(0)
  t.goto(x, y)
  t.pendown()
  t.begin_fill()
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.left(90)
  t.forward(w)
  t.left(90)
  t.forward(h)
  t.end_fill()
  t.penup()

def luoEsteet(n):
  t = turtle.Turtle()
  t.speed("fastest")
  t.color("red")
  
  suorakulmiot = []
  for i in range(n):
    x = random.randint(-maxleveys, maxleveys)
    y = random.randint(-maxkorkeus, maxkorkeus)
    w = random.randint(10, 300)
    h = random.randint(10, 300)
    
    piirraSuorakulmio(t, x, y, w, h)
    
    suorakulmiot.append((x, y, w, h))
    
  t.hideturtle()
  return suorakulmiot
    
def onkoSuorakulmionSisalla(x, y, suorakulmio):
  return (x >= suorakulmio[0] and x < suorakulmio[0] + suorakulmio[2] and
          y >= suorakulmio[1] and y < suorakulmio[1] + suorakulmio[3])

def onkoJonkinSuorakulmionSisalla(x, y, suorakulmioLista):
  for suorakulmio in suorakulmioLista:
    if onkoSuorakulmionSisalla(x, y, suorakulmio):
      return True
  return False

def onkoPiirtoalueenUlkopuolella(x, y):
  return x < minleveys or y < minkorkeus or x >= maxleveys or y >= maxkorkeus

def teeLiike(suorakulmiot):
  x = t.xcor()
  y = t.ycor()
  
  if onkoPiirtoalueenUlkopuolella(x, y):
    t.right(180)
  elif onkoJonkinSuorakulmionSisalla(x, y, suorakulmiot):
    t.right(180)
  else:
    t.right(random.randint(-30, 30))
    
  t.forward(10)

##### TEHTÄVÄ #####

# Klikkaa 'Run' ja katso mitä tapahtuu
# Klikkaa 'Run' uudelleen saadaksesi uudet esteet
# Jos kilpikonna jää heti jumiin, klikkaa 'Run' uudelleen

suorakulmiot = luoEsteet(10)

# Animaatio alkaa tästä
while True:
  teeLiike(suorakulmiot)


# 1. Muokkaa teeLiike funktiota siten, että kilpikonna jatkaa suoraan
# eteenpäin joutuessaan suorakulmion sisälle.

# 2. Muokkaa teeLiike funktiota siten että kilpikonna tekee aina
# t.right(10) joutuessaan suorakulmion sisälle.

# 3. Muokkaa teeLiike funtiota siten että kun kilpikonna ensimmäisen
# kerran päätyy suorakulmion sisään, jatkaa se liikettään vain
# suorakulmioiden sisällä eikä mene enää valkoiselle alueelle.

##### LISÄTEHTÄVÄ #####

# Korvaa luoEsteet() fuktio omalla funktiollasi,
# joka piirtää labyrintin satunnaisten suorakulmioiden sijaan.
# Löytääkö kilpikonna ulos labyrintistasi?
