import turtle
t = turtle.Turtle()


##### TEHTÄVÄ 1 #####
# Täytä funktiot siten että pystyt piirtämään 3D heksaedrin
# eli suorakulmaisen särmiön
#
# Tältä sivulta löydät esimerkin halutusta kuviosta:
# https://fi.wikipedia.org/wiki/Suorakulmainen_s%C3%A4rmi%C3%B6
#
# Huomaa että sinun tulee käyttää funktion parametreja
# w: leveys
# h: korkeus


# Täytä tähän funktio, joka piirtää etutahkon
def etu_tahko(w, h):
  print(u"Tämän funktion tulee piirtää suorakulmaisen särmiön etupuoli")


# Täytä tähän funktio, joka piirtää ylätahkon
def yla_tahko(w, d):
  print(u"Tämän funktion tulee piirtää suorakulmaisen särmiön yläpuoli")


# Täytä tähän funktio, joka piirtää oikean tahkon
def oikea_tahko(h, d):
  print(u"Tämän funktion tulee piirtää suorakulmaisen särmiön oikea puoli")


def heksaedri(w, h, d):
  etu_tahko(w, h)
  yla_tahko(w, d)
  oikea_tahko(h, d)

t.penup()
t.goto(0, -200)
t.pendown()
heksaedri(50, 50, 50)


##### TEHTÄVÄ 2 #####
# Kun olet toteuttanut funktiot, voit piirtää minkä tahansa kokoisen
# suorakulmaisen särmiön tahansa.
# Kokeile poistaa kommentit alla olevista komennoista ja katso mitä tapahtuu

#heksaedri(200, 100, 200)
#heksaedri(70, 100, 200)
