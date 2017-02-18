# Auta kilpikonnaa löytämään reikä seinässä

import turtle

##### INFO #####
#
# Seuraava koodi piirtää seinän ja maalin. Voit katsoa
# koodin läpi, mutta sinun ei tarvitse ymmärtää kaikkea
# tätä. Vieritä alaspäin varsinaiseen tehtävään.

# Tämä kilpikonna nimeltään wall piirtää seinän ja maalin.
wall = turtle.Turtle()
wall.hideturtle()
wall.speed("fastest")
wall.width(4)
wall.penup()
wall.setx(100)
wall.sety(110)
wall.pendown()
wall.sety(-500)
wall.penup()
wall.sety(140)
wall.pendown()
wall.sety(500)
wall.penup()
wall.right(90)
wall.forward(420)
wall.setx(200)
wall.dot(20, "red")

# Tässä luodaan toinen kilpikonna nimeltä Joe.
joe = turtle.Turtle()
joe.shape("turtle")

# Joe lähtee kuljeskelemaan.
joe.right(120)
joe.forward(100)
joe.right(90)
joe.forward(50)

##### TEHTÄVÄ #####
#
# Paina Run-nappia nähdäksesi minne Joe on menossa. Ohjaa
# Joe punaisen pisteen luokse. Älä koske seinään!
#
# Kirjoita käskyt tänne:
