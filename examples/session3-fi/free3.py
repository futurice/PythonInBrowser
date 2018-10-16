# Piirretään satunnaisilla väreillä

##### INFO #####
# Käytä kaikkia tähän mennessäsi oppimiasi konsepteja:
# satunnaisuutta (random), for-looppia ja funktioita

import turtle  # muista tuoda kilpikonna aina kun haluat piirtää

import random  # satunnaisuus (random) pitää myös importtaa

t = turtle.Turtle()
t.speed("fastest")

# Muokataan piirtoalueen taustaväriä
# Voimme asettaa uuden värin seuraavasti
turtle.Screen().bgcolor("black")

# Piirretään useilla väreillä.
# Voimme määritellä eri värejä listassa
variPaletti = ["red", "blue", "green", "yellow", "orange", "brown", "purple", "pink"]

# Listasta voi valita värin indeksillä
variPaletista = variPaletti[0]  # 'variPaletista' muuttujan arvo on nyt "red" eli punainen

# Nyt päästään hauskaan osuuteen: valitaan väri satunnaisesti
# Määritellään ensin mikä on 'variPaletti' -listan viimeinen indeksi
viimeisenVarinIndeksi = len(variPaletti) - 1

# Satunnainen väri voidaan nyt valita seuraavasti.
# Säilötään se muuttujaan 'satunnainenVari'
satunnainenVari = variPaletti[random.randint(0, viimeisenVarinIndeksi)]

##### TEHTÄVÄ #####
# Kommentoi rivi 23: turtle.Screen().bgcolor("black")
# ja poista kommenti seuraavalta riviltä
# turtle.Screen().bgcolor(satunnainenVari)

# Määritellään funktio, joka piirtää neliöitä, mutta hieman yli 90 asteen
# kulmalla - tällöin se muodostaakin ympyröitä. Vaihdetaan myös väriä
# jokaisen neliön jälkeen.

##### FUNKTIO ALKAA #####
def varikasOlympiaKeha():
  t.forward(80)
  t.left(92)
  uusiVari = variPaletti[random.randint(0, len(variPaletti) - 1)]
  t.color(uusiVari)
##### FUNKTIO LOPPUU #####

# Ylläoleva funktio ei vielä yksinään tee mitään.
# Käytetään sitä seuraavaksi piirtämiseen

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

# Opimme nyt uuden asian: sisäkkäiset loop -silmukat
# Esimerkki alla toistaa 5 kertaa 100 kutsua funktioon 'varikasOlympiaKeha'

# Ulompi loop-silmukan osa toistetaan 5 kertaa
for i in range(5):
  # Sisempi loop-silmukan osa toistetaan 100 kertaa
  for i in range(100):
    varikasOlympiaKeha()
  # Seuraava osuus on taas osa ulompaa silmukkaa
  # Huomaa sisennys!
  t.penup()
  t.left(90)
  t.forward(200)
  t.pendown()

# Kokeile listätä seuraava rivi funktion viimeiselle riville.
# turtle.Screen().bgcolor(uusiVari)
# Muista tarkistaa että olet sisentänyt funktion oikein

# Voit nyt muokata koodia miten haluat. Lisää ympyröitä, muuta muotoja ja värejä
# ja niin edelleen.

