# Ympyrän kehä

##### INFO #####
# Mikä on ympyrän ympärysmitta?
# Voimme arvioida pituutta piirtämällä tasasivuisen monikulmion ympyrän sisälle
# ja mittaamalla monikulmion ympärysmitan. Mitä monisivuisempaa
# monikulmiota käytämme, sitä tarkemman arvion saamme.
#
# Ympyrän ympärysmittaa kutsutaan kehän pituudeksi.

# Seuraava koodi valmistelee tehtävän.

import turtle
from math import cos, sin,  pi, sqrt

# Piirrä ympyrä
r = 200
circle = turtle.Turtle()
circle.speed('fastest')
circle.hideturtle()
circle.penup()
circle.color('red')
circle.goto(0, -r)
circle.pendown()
circle.circle(r)

# Seuraava funktio piirtää tasasivuisen monikulmion ympyrän sisälle.
# Parametri n ilmaisee määrittää kuinka monta sivua monikulmiolla on.
# Funktio palauttaa monikulmion ympärysmitan.
def monkulmio(n):
  # Laita kilpikonna valmiiksi
  t = turtle.Turtle()
  t.penup()
  t.speed('fastest')
  t.goto(0, r)
  t.right(180.0/n)
  t.speed(6)
  t.pendown()

  # Laske monimulmion sivun pituus
  askel = 2 * r * sin(pi/n)

  # Draw the polygon and record its perimeter
  etaisyys = 0
  for i in range(n):
    etaisyys = etaisyys + askel
    t.forward(askel)
    t.right(360.0/n)
    
  return etaisyys

todellinen_kehan_pituus = 2 * pi * r

##### TEHTÄVÄT #####
# monikulmio(3) piirtää kolmion. Paina Run ja katso mitä tapahtuu!
#
# Kokeile lisätä sivujen määrää (luku sulkujen sisällä) ja tarkastele
# miten monikulmio vastaa ympyrän kehää paremmin ja paremmin.

monikulmion_piiri = monkulmio(3)

print u"Monikulmion piiri: " + str(monikulmion_piiri )
print u"Ympyrän kehän todellinen pituus: " + str(todellinen_kehan_pituus)
print u"Erotus: " + str(todellinen_kehan_pituus - monikulmion_piiri)

# Kuinka monta sivua monikulmiolla tulee olla, jotta erotus todelliseen
# kehän pituuteen on vähemmän kuin 1% kehän todellisesta pituudesta?
# (katso viimeistä printtausta)

# Kuinka monta sivua vaaditaan, että et enää erota monikulmiota ympyrän
# kehästä?


##### LISÄTIETOA #####

# Monikulmion piirillä saadaan approksimoitua ympyrän kehää mielivaltaisen
# läheltä, kun monikulmion sivujen määrää n kasvatetaan kohti äärettömyyttä.
# Tämän todistaminen vaatii jo kehittyneempiä matemaattisia työkaluja.