## Printtailu ja laskutoimitusharjoituksia
print u"Terve jälleen!"
print u"Nyt lasketaan: 77 + 89 = ", 77+89 

## Python on ohjelmointikieli, jota voi tietenkin käyttää myös laskimena
# print 5+6


########################################################
## TEHTÄVÄ 1:
## Poista alla rivien aluista kommenttimerkit, eli nuo häshtägit (#).
## Miksi? Koska Python tulkki jättää huomiotta kaiken #:n jälkeen.

# print 1.0/2.0
# print 2.5/5
# print 5/3.0

########################################################
## TEHTÄVÄ 2:
## Keksitkö mikä matemaattinen operaatio on "**"?
## Vihje: Muuttele numeroita.

# print 3.0 ** 2.0


########################################################
## TEHTÄVÄ 3:

## Huom: import -komento on Pythonin perusteita.
import math  # otetaan Pythonin matematiikka kirjasto käyttöön.

## Mutta mistä tietää mitä "math":in sisältä löytyy? -> KVG

# print "sin(0) = ", math.sin(0)
# print "sin(0) = ", math.sin(math.pi * 2)
# print "sin(pi) = ", math.sin(math.pi)


########################################################
## TEHTÄVÄ 4:
## Tutkitaan trigonometrian perusyhtälöä:

# print "sin(x)^2 + cos(x)^2 = ???"

## Tässä luodaan muuttuja, jolle annetaan arvo.
luku = 0.77
## Muuttujat helpottavat ohjelmointia. Osaatko selittää miksi?

## Nyt itse asiaan:
# print math.pow(math.sin(luku), 2) + math.pow(math.cos(luku), 2)



########################################################
## BONUS:
## Entä tämä, mikä matemaattinen operaatio on "%"?

# print 4.0 % 3.0
