# Drawing lines

import coordinates
import turtle

coordinates.prepareCoordinates()
t = turtle.Turtle()

##### INFO #####
# Matematiikassa suoran yhtälö annetaan ylensä muodossa y = kx + b
# Halaumme piirtää kilpikonnalla suoran piirrustusalueelle.
# Ensin meidän täytyy muuttaa yhtälö muotoon, jota koodi ymmärtää.
# Teemme sen funktiolla nimeltä viiva

def viiva(k, b):
  # Nostamme kynän
  t.penup()

  # "for" jokaiselle x:lle välillä -550:stä 550:een teemme seuraavan
  for x in range(-550, 550):
    # menemme pisteeseen (x, k*x + b)
    t.goto(x, k * x + b)
    # laitamme kynän alas ja alamme piirtää
    t.pendown()

# Katsotaan miten tämä toimii: Piirretään suora y = 2x
# Teemme sen seuraavasti
viiva(2, 0)

##### TEHTÄVÄ #####
# 1. Piirrä suora y = -0.5 x + 50
viiva(-0.5, 50)

# 2. Piirrä suora y = x - 100
viiva(1, -100)

# 3.Piirrä haluamasi suora
# Kirjoita ensin yhtälö ja kutsu sitten funktiota line haluamillasi arvoilla
