# Monikulmion piiri

import turtle

##### INFO #####
# Monikulmion piiri on matka jonka kilpikonna kulkee piirtäessään suljetun
# monikulmion.

# Alla on apufunktio, joka siirtää kilpikonnan koordinaatteihin
# (x, y), mutta ei piirrä viivaa.
def siirra_kilpikonna(t, x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  return t

# Funktio joka pirtää neliön ja palauttaa sen piirin
#
# Parametri 't' on kilpikonna.
# Parametri 'sivu' kertoo kuinka pitkä neliön sivu on.
def nelio(t, sivu):
  distance = 0
  for i in range(4):
    distance = distance + sivu
    
    t.forward(sivu)
    t.right(90)
  
  return distance

# Käytetään nelio funktiota piirtämään neliö, jolla on 100
# pituiset sivut; ja printataan neliön piiri.
t = turtle.Turtle()

siirra_kilpikonna(t, -50, 150)
nelion_piiri = nelio(t, 100)
print u"Neliön piiri: " + str(nelion_piiri)

##### TEHTÄVÄT #####

##### TEHTÄVÄ 1 #####
# Viimeistele seuraava funktio niin että see piirtää tähden.
# Jokaisen sivun tulee olla yhtä pitkä ja parametri 'sivu'
#  määrittelee pituuden.
#
# Funktion paluuarvon tulee olla tähden piiri.

def tahti(t, sivu):
  etaisyys = 0
  
  etaisyys = etaisyys + sivu
  t.forward(sivu)
  
  t.right(120)
  etaisyys = etaisyys + sivu
  t.forward(sivu)
  
  t.left(60)
  etaisyys = etaisyys + sivu
  t.forward(sivu)

  t.right(120)
  etaisyys = etaisyys + sivu
  t.forward(sivu)
  
  t.left(60)
  etaisyys = etaisyys + sivu
  t.forward(sivu)
  
  t.right(120)
  etaisyys = etaisyys + sivu
  t.forward(sivu)

  t.left(60)
  etaisyys = etaisyys + sivu
  t.forward(sivu)


  # LISÄÄ KOODISI TÄHÄN

  # Muista lisätä kuljettu matka etaisyys muuttujaan aina
  # kun liikutat kilpikonnaa eteenpäin.
  #
  # Vinkki: voin välttää toistoa käyttämällä loop-silmukkaa

  return etaisyys

siirra_kilpikonna(t, -50, 0)
tahti_piiri = tahti(t, 100)

print u"tähden ympärysmitta: " + str(tahti_piiri)


##### TEHTÄVÄ 2 #####
# Kuinka pitkä tähden sivun pitäisi olla, jotta sen ympärysmitta olisi
# sama kuin neliöllä?
#
# Joko kokeile eri sivun pituuksia funktioilla tai mieti kynällä ja
# paperilla.
