# Piirretään kolmio käyttäen muuttujaa

import turtle
t = turtle.Turtle()
t.shape("turtle")

##### INFO #####
#
# Piirretään kolmio jonka sivun pituus on 150 pikseliä.
#
# Määritellään muuttuja, joka kertoo kolmion sivun pituuden:

sivu = 150

# Jatkossa voit käyttää koodissa sanaa sivu ja komentoa
# suorittaessaan tietokone käyttäytyy ikäänkuin sen tilalla
# olisi luku 150.
#
# Tarkastellaan muuttujan määrittelyä tarkemmin:
#
# sivu on muuttujalle annettava nimi. Se voi olla mikä
# tahansa sana kunhan se ei sisällä ääkkösiä. Myöskään pari
# ohjelmoitikielen käyttöön varattua sanaa kuten 'import'
# eivät ole mahdollisia nimiä.
#
# = tarkoittaa että jatkossa yhtäsuuruusmerkin vasemmalla
# puolella oleva nimi tarkoittaa samaa kuin
# yhtäsuuruusmerkin oikealla puolella oleva lukuarvo.
#
# 150 on arvo, jonka haluamme antaa muuttujalle.

##### TEHTÄVÄ #####
#
# Tämä koodi pirtää kolmion. t.forward(sivu) siirtää
# kilpikonnaa eteenpäin 150 pikseliä, koska määrittelimme
# aikaisemmin että sivu tarkoittaa lukua 150.
#
# Paina Run-nappia!

t.forward(sivu)
t.left(120)
t.forward(sivu)
t.left(120)
t.forward(sivu)

# Piirrä pienempi kolmio vaihtamalla rivillä 13 luvun 150
# paikalle luku 60. Paina taas Run-nappia.
#
# Muuttujaa käyttäen kolmion uusi sivun pituus tarvitsee
# kirjoittaa vain yhteen paikkaan eikä erikseen jokaiseen
# t.forward-komentoon.
#
# Kokeile vielä piirtää erikokoisia kolmioita vaihtamalla
# lukua rivillä 13. Mikä on suurin kolmio, joka mahtuu
# kokonaan ruudulle?
