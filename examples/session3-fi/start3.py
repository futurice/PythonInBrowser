# Kerrataan mitä opimme viime viikolla
# Jos jokin asia mietityttää, kysy vain rohkeasti apua!

##### INFO #####
# Viimeksi opimme seuraavat funktiot:
# Goto, pendown, penup, color
# Opimme myös kirjoittamaan For-silmukan

import turtle
t = turtle.Turtle()

def lehti(x):
  if x == 0:
    return
  else:
    t.forward(x/10.0)
    t.right(10)
    lehti(x - 1)

# Olemme määritelleet valmiiksi funktion lehti, jota voit käyttää koodissasi.
# Opimme lisää funktioista tällä viikolla

##### TEHTÄVÄT #####
# 1.
# Mene pisteeseen (-200, 200) ja valitse haluamasi väri.
# Piirrä lehti kuusi kertaa arvolla 102

# 2.
# Mene pisteeseen (-50, 30) ja vaihda uuteen väriin
# Piirrä lehti kuusi kertaa arvolla 102.

# 3.
# Mene pisteeseen (100, -100) ja vaihda taas uusi väri
# Piirrä taas lehti kuusi kertaa arvolla 102

# Huom! Et halua että piirtoalueella näkyy muuta kuin lehti funktion piirtämä osuus
# Käytä siis funktioita penup ja pendown sopivissa kohdin


# 4.
# Piirrettyäsi kohdat 1-3 katso taas koodiasi
# Onko kohtia joita toistat uuselleen ja uudelleen?
# Seuraavassa tehtävässä opimme korjaamaan tämän!
