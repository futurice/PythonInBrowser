# Funktioiden kertaus
import turtle
t = turtle.Turtle()

##### TEHTÄVÄ #####

##### TEHTÄVÄ 1 #####
# Kutsu funktiota moi eri nimillä.
# Kutsu sitten funktiota kolmio sivun eri pituuksilla.
# Selitä itsellesi tai kaverille mitä funktion kutsuminen tarkoittaa

def moi(nimi):
  print "Moi " +  nimi + "!"

def kolmio(sivu):
  for i in range(0, 3):
    t.forward(sivu)
    t.right(120)


##### TEHTÄVÄ 2 #####
# Täydennä funktio nimeltä kerroYhteen
# Testaa sitten että se toimii odotetusti kutsumalla testaaKerroYhteen -funktiota

def kerroYhteen(x, y):
  # TÄYTÄ KOODISI TÄHÄN
  # Vinkki: Haluat palautaa jotain muuta kuin 0
  return 0

def testaaKerroYhteen():
  arvo1 = kerroYhteen(5, 6)
  if arvo1 == 30:
    print u"funktio toimii, 5 * 6 = 30"
  else:
    print u"Ups! Jotain meni pieleen funktiossa."
    print "5 * 6 != " + str(arvo1)

  arvo2 = kerroYhteen(385, 525)
  if arvo2 == 202125:
    print u"funktio toimii, 385 * 525 = 202 125"
  else:
    print u"Ups! Jokin meni pieleen funktiossa."
    print "385 * 525 != " + str(arvo2)


##### TEHTÄVÄ 3 #####
# Kirjoita oma funktiosi
# Asioita mitä sinun tulee päättää:
#  - funktion nimi
#  - ottaako funktio parametreja
#  - mitä funktio tekee? Printaako, laskeeko, piirtääkö tai palauttaako se jotain? (Vai jopa kaikkea tätä?)
