# Lukujonot

import turtle

##### INFO #####
#
# Loop-silmukkaa voi käyttäää lukujonon numeroiden laskemiseen

##### TEHTÄVÄ #####

# Keksitkö mitkä ovat seuraavan lukujonon seuraavat luvut?
# Lisää seuraavat 4 lukua.
[4, 7, 10]


# Pitkän lukujonon laskeminen käsin on tylsää. Laitetaan kone
# tekemään tämä puolestamme.
#
# Seuraava loop-silmukka laskee 20 ensimmäistä lukua samaisesta jonosta.

luku = 4
lukujono = [luku]

for i in range(20):
  luku = luku + 3
  print u'Lisätään luku', luku, u'lukujonoon'
  lukujono.append(luku)


# Seuraavat komennot eivät ole osa loop-silmukkaa, koska niitä
# ei ole sisennetty.
  
print u'Loop-silmukan jälkeen lukujono on seuraava'
print lukujono

# Piirretään jotain käyttäen juuri laskemaamme lukujonoa.
# Poista kommentointi seuraavien rivien edestä:

# t = turtle.Turtle()
# for s in lukujono:
#   t.forward(s)
#   t.right(60)

# Muuta lukujonoa (joka laskettiin ensimmäisessä loop-silmukassa)
# tai kulmaa r.right(60) toisessa loop-silmukassa) ja katso mitä tapahtuu.
