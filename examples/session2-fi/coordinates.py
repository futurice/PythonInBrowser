# Piirrä pisteitä koordinaattisysteemissä

import coordinates
import turtle

# Alusta koordinaatit ja kilpikonna
coordinates.prepareCoordinates()
t = turtle.Turtle()

##### INFO #####
# Seuraavaksi opimme uusia komentoja kilpikonnalle
#
# Penup:
# t.penup(), tarkoittaa että nostamme kynän ylös ja vain siirrämme kilpikonnaa piirtämättä
#
# Pendown:
# t.pendown(), laskee kynän takaisin alas ja jatkaa piirtämistä
#
# Goto:
# t.goto(10, 20), siirtää kilpikonnan nykyiseltä sijainnilta sijaintiin (10, 20)
#
# Dot:
# t.dot(2), piirrä pieni piste nykyiseen sijaintiin
#
# Home:
# t.home(), siirry takaisin sijaintiin (0,0)

##### TEHTÄVÄ #####
# 1. Kokeile näitä komentoja vapaasti
t.forward(100)
t.right(30)
t.penup()
t.forward(200)
t.dot(5)
t.pendown()
t.right(90)
t.forward(50)
t.home()

# 2. Aja seuraava koodi ja katso mitä tapahtuu.
# Korjaa se lisäämällä sopiviin kohtiin t.pendown() ja t.penup()
# niin että lopullisessa kuvassa on vain sininen neliö

#t.color("blue")
#t.goto(-150, 0)
#t.goto(0, 150)
#t.goto(0, 0)
#t.goto(150, 0)
#t.goto(0, -150)
#t.goto(0, 0)
#t.goto(-150, 0)
#t.goto(0, -150)
#t.goto(0, 0)
#t.goto(150, 0)
#t.goto(0, 150)
#t.goto(0, 0)


