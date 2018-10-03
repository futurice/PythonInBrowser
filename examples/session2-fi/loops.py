# Loopit eli silmukat

##### INFO #####
#
# Joskus monimutkaisen kuvion piirtäminen vaatii samojen
# komentojen toistamista moneen kertaan. Loopilla eli silmukalla
# voit toistaa koodipalikoita eli pätkiä koodia

import turtle
t = turtle.Turtle()

# Seuraava on esimerkki silmukasta.
#
# "for" kertoo tietokoneelle että sen tulee toistaa jotakin
# monta kertaa
#
# "in range(2)" kertoo että komento tulee toistaa 2 kertaa
#
# "i" on muuttuja jonka arvo kasvaa yhdellä jokaisen toiston
# (eli iteraation) jälkeen. Muuttujaa i ei käytetä tässä
# tehtäväss, mutta näet myöhemmin esimerkkejä, joissa siitä
# on hyötyä.

for i in range(2):
  # Seuraavilla riveillä on komennot jotka toistetaan.
  # Nämä rivit ollaan sisennetty, eli ne alkavat kahdella välilyönnillä
  # Sisennyksellä kerrotaan mitkä rivit kuuluvat toistettavaan koodipalikkaan.
  t.forward(30)
  t.left(120)
  t.forward(30)
  t.right(60)

##### TEHTÄVÄ 1 #####
#
# Klikkaa 'run' ja katso mitä tapahtuu.
#
# Kuinka monta kertaa silmukka tulisi toistaa että tähti olisi valmis?
# Laita oikea numero komennon range(...) sulkujen sisään.
# Vinkkin: voit kokeilla useita eri numeroita ja katsoa mikä toimii

##### TEHTÄVÄ 2 #####
#
# Mieti muita muotoja joissa on toistuva kaava.
# Esimerkiksi: neliö, rappuset, aallot
#
# Muuta silmukkaa niin että se piirtää valitsemasi kuvion.
#
# Vinkki: Aloita piirtämällä vain yksi toisto kirjoittamalla
# "range(1)" ja saa se piirtämään kuten haluat. Voit sitten
# toistaa kuvion niin monta kertaa kuin haluat muuttamalla
# range arvoa.
