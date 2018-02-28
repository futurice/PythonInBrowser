################################################
## RANDOM KIRJASTO

## random on yksi Pythonin peruskirjastoista

import random

## Tässä alustetaan näennäissatunnaislukugeneraattori.


## Luodaan dataa. Mikä datastruktuurityyppi on kyseessä?
dataa = ["kissa", "koira", "makkara"]


## Satunnainen valinta datastruktuurista:

#print random.choice(dataa)


## Satunnainen kokonaisluku

#print random.randint(1, 100)


## kuusitahoinen noppa

# Tämä arpoo kolme lukua väliltä 1-6 joka kerta, kun painat run-nappia.

# heittotulokset = []
# for _ in range(3):
#     heittotulokset.append(random.randint(1, 6))

# print u'Heitetään noppaa:'
# print heittotulokset


## Tehtävä: Laske silmälukujen keskiarvo, kun noppaa heitetään 1000 kertaa.
