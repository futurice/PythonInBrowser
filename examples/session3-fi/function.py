# Funktioilla laskeminen

import turtle
t = turtle.Turtle()

##### INFO #####
# Funktioita voidaan käyttää asioiden laskentaan.
#
# Otetaan esimerkkinä ympyrän pinta-alan laskeminen.
# Saatat muistaa matematiikan tunnilta, että ympyrän
# pinta-ala lasketaan kertomalla ympyrän säde itsellään ja
# luvulla pii.
#
# Pii on matemaattinen vakio. Sen likiarvo on määritelty alla:

pi = 3.14159265359

# Voimme nyt laskea ympyrän, jonka säde on 15, pinta-alan seuraavasti:

pintaala15 = pi * 15 * 15
t.circle(15)
print u'Ympyrä, jonka säde on 15, pinta-ala on ' + str(pintaala15)

# Vähän isomman ympyrän, jonka säde on 22, pinta-ala on:

pintaala22 = pi * 22 * 22
t.circle(22)
print u'Ympyrä, jonka säden on 22, pinta-ala on: ' + str(pintaala22)

##### TEHTÄVÄT #####

##### TEHTÄVÄ 1 #####
# Mikä on ympyrän, jonka säde on 30, pinta-ala?


##### TEHTÄVÄ 2 #####
# Määritellään funktio, joka laskee ympyrän pinta-alan

def ympyran_pintaala(sade):
  return pi * sade * sade

# "return" eli palauta tarkoittaa että funktio päättyy ja
# return avainsanan jälkeinen osuus palautettaan funtiota
# kutsuneelle osalle koodia
#
# Funktio ympyran_pintaala ottaa yhden parametrin nimeltä sade.
# Parametrin sade arvo annetaan funktiolle sulkujen sisällä.
# Esimerkiksi jos haluamme säteen olevan 15, kirjoitamme:
# ympyran_pinta_ala(15).

# Voimme nyt käyttää kyseistä funktiota laskemaan (taas)
# 15-säteisen ympyrän pinta-alan. Asetetaan funktion paluuarvo
# muuttujaan pintaala15_funktiolla ja printataan sen arvo:

pintaala15_funktiolla = ympyran_pintaala(15)
print u'15-säteisen ympyrän pinta-ala laskettuna funktiolla on ' + str(pintaala15_funktiolla)

# 1. Tarkista että saamasi arvo on sama kuin esimmäisessä tehtävääs.


# 2. Laske 22-säteisen ympyrän pinta-ala käyttäen funktiota


# 3. Laske 30-säteisen ympyrän pinta-ala käyttäen funtiota



##### LISÄTEHTÄVÄ #####
# Funktioita voidaan käyttää myös merkkijonojen muokkaamiseen.
# Seuraava funktio laskee kuinka monta vokaalia merkkijonossa on.

def laske_vokaalit(text):
  count = 0
  for letter in text:
    if letter.lower() in u"aeiouyöä":
      count = count + 1
  return count

# Seuraava rivi laskee kuinka monta vokaalia sanassa "Python" on
# Poista seuraavan rivin kommentointi
# print u'Sanassa "Python" on vokaaleja: ": ' + str(laske_vokaalit("Python"))

# 1. Keksitkö sanan jossa on 5 vokaalia? Entä 6 tai enemmän?

# 2. Kirjoita funktio, joka laskee kuinka monta konsonattia
# sanassa on. Konsonantteja ovat kirjaimet, jotka eivät ole vokaaleja.
# Keksi sitten sanoja joissa on mahdollisimman monta konsonanttia