################################################
## SEKVENSSIT JA FOR-LOOPIT

## Datastruktuureista lisää:
## https://docs.python.org/2/tutorial/datastructures.html

################################################
## LISTA (aka list())
## on yksi sekvenssi-datastruktuureista
## Stringi taas on kasa kirjainmerkkejä.
muuttuja = u"tämä on string -tyyppinen muuttuja. tämä teksti on siis string!"

sekvenssi = [
    u'Tämä on lista stringejä.',
    u'Eli lista aloitetaan hakasuluilla []',
    u'ja sen sisältämät elementit erotellaan pilkuilla.',
    u'kuten varmaan huomaat!!',
    u'No mutta miten tätä käytetään?'
]

## Voimme printata yllä luodun listan
#print sekvenssi


## Listasta voi myös printata yksittäisiä elementtejä (nolla on ensimmäinen!)
#print ""
#print sekvenssi[0]
#print sekvenssi[3]
#print sekvenssi[-1]  # protip: -1 on viimeinen elementti
#print sekvenssi[1:4]  # tämä valitsee elementit 1, 2, 3 (viimeistä ei oteta)

## BONUS
## Mitä käy jos yrität printata elementin 1000, kun sekvenssissä on vain 5 elementtiä?


## Listaan lisätään elementtejä append():illa ja poistetaan pop():illa
#sekvenssi.append(u'Yksi lisää loppuun')
#print sekvenssi[5]
#print sekvenssi[-1]

#sekvenssi.pop(5)
#print sekvenssi[-1]


################################################
## JOUKKO (aka set())
## Toinen kätevä Sekvenssi-tyyppinen kaverus.
##
## Vähän niinkuin lista, mutta jokainen elementti on uniikki:

#setti = set(1, 3, 4, 78)
#print setti
#setti.add(5)
#print u"Joukko lisäyksen jälkeen:", setti
#setti.add(5)
#print u"Jo olemassaolevan elementin lisääminen ei muuta joukkoa:", setti

## Joukon elementit voivat olla myös stringejä
#sanat = set("makkara", "peruna", "porkkana")
#print sanat

## Joukkoon lisätään metodilla "add()"
#sanat.add("titaani")
#print sanat
## Mitä käy jos yrität lisätä kuin listaan?
#sanat.append("banaani")


## Listasta joukko
#listunen = ["kana", "kana", "kana", "kukko", "kana", "kissa"]
#joukkonen = set(listunen)
#print listunen
#print joukkonen
#print u"Näet varmaan eron listan ja setin välillä?"


## HUOM: Menetkö sekaisin mistä nimet "setti", "sanat" ja "set" tulevat?
##
## Ohjelmoinnissa osa nimistä on varattu kielen perusteisiin,
## osa kirjastoille, ja loput ohjelmoijat saavat keksiä itse.


################################################
### FOR-looppi
## Esittelimme listan (joka on yksi sekvensseistä), koska se on kätevä tapa
## pitää lauseita tietokoneen muistissa.
## Kätevän siitä tekee se, miten sekvenssin
## sisältämiä elementtejä voi iteroida.
##
## Sekvenssejä käydään läpi for-loopilla:

#sekvenssi = list(2, 3, 4, 5, 6)
## tai
#sekvenssi = [2, 3, 4, 5, 6]  # kaksi ekvivalenttia tapaa luoda lista Pythonissa
#for elementti in sekvenssi:
#    print 'Jee:', elementti

## HUOM: for-loopin jälkeinen sisennys!
## Tärkeä Python kielen ominaisuus.


## Loopin sisällä sekvenssin elementeille voi
## "tehdä jotain" yksi toisensa jälkeen. Hieno homma!


################################################
## Tehtäviä??
## Luo joukko, ja käytä for-looppia siihen. Toimiiko samoin kuin lista?

