## Ilmiö: Kalevala
##
## Ideana tutkia luonnollisen tekstin käsittelyä (LTK, aka NLP).
## Tutkitaan Kalevalan tekstiä Pythonilla.
##
## Kalevala tiedostoina (latin-1):
## http://www.sci.fi/~alboin/trokeemankeli/kalevalamitta-aineistoja.htm



## Ladataan Kalevalan teksti

# TODO: make it VIA IMPORTS - DOESN't WORK??

# from datasets import kalevala as kale_txt


## Ladattu teksti on "lista" (list) stringejä.

# TODO: remove this after import kalevala works
sekvenssi = [
    u'Tämä on lista stringejä.',
    u'Eli lista aloitetaan hakasuluilla []',
    u'ja sen sisältämät elementit erotellaan pilkuilla.',
    u'kuten varmaan huomaat!!',
    u'No mutta miten tätä käytetään?'
]


##################################################
## TEKSTIN KIMPPUUN
## Nyt perusteet on käyty. (sekvenssi ja for-looppi)


###############
## 01: Miltä teksti näyttää

kale_txt = sekvenssi

#print kale_txt[0]
#print kale_txt[100]
#print kale_txt[0:5]
#print '\n'.join(kale_txt[0:5])


###############
## 02: Lasketaan juttuja meidän Kalevala tekstistä

#print u"Näin monta riviä:", len(kale_txt)
#print u"Ekalla rivillä näin monta merkkiä:", len(kale_txt[0])

#print u"Miten laskisit kuinka monta merkkiä koko Kalevalassa on?"


###############
## 03: Kuinka monta ?-merkkiä löytyy?

## Vastausesimerkki; käydään jokaisen rivin jokainen merkki yksitellen läpi:
#haluttu_merkki = '?'
#summa = 0
#for rivi in kale_txt:
#    for merkki in rivi:
#        if merkki == haluttu_merkki:
#            summa += 1
#print u"Näin monta ", haluttu_merkki, u"-merkkiä: ", summa

## Esim2; käytetään Pythonin kieltä "Pythonmaisemmin"
#print sum([x.count(haluttu_merkki) for x in kale_txt])


###############
## 04: Kuinka monta sanaa löytyy? Tai mitä sanoja löytyy?

## Otetaan käyttöön "joukko", eli set() (toinen Sekvenssi-tyyppinen muuttuja).
## TODO: tutustuminen set -tyyppiin

#kaikki_sanat = set()
#for rivi in kale_txt:
#    for sana in rivi.split():
#        kaikki_sanat.add(sana)
#print(kaikki_sanat)




## "def" -avainsanalla luodaan kutsuttavia metodeja.
## TODO: tutustuminen metodeihin


def clean_text_line(line):
    u"""Siivotaan rivi tekstiä
    Nämä päätökset perustuvat
    tekstin tutkimiseen yllä.
    """
    return (
        line
        .lower()
        .replace('--', '')
        .replace('"', '')
        .replace(';', '')
# välilyönnin lisääminen tekee merkeistä erillisiä
        .replace('\n', ' \n')
        .replace(',', ' ,')
        .replace('.', ' .')
        .replace('?', ' ?')
        .replace('!', ' !')
    )


def clean_up(kale_txt):
    u"""Siivotan Kalevala"""
    fixed_kale = list()
    words = list()
    # fiksaillaan ja uudelleen muotoillaan tekstiä
    for line in kale_txt:
        clean_line = (clean_text_line(line))
        # laitetaan kaikki sanat yhteen pötköön
        for word in clean_line.split():
            words.append(word)
    print(len(words), 'words after splitting.')
    return words


def do_stats(words):
    u"""Lasketaan sanojen statistiikkaa"""
    stats = dict()
    # Käydään läpi kaikki sanat.
    # Muodostetaan hakemisto, jossa:
    #  *key on sana A,
    #  *value on toinen hakemisto, jossa
    #   -key on A:ta seuraava sana, B
    #   -value on kuinka monta kertaa
    #    B on seurannut A:ta koko tekstissä
    for n in range(0, len(words)-1):
        current_word = words[n]
        next_word =words[n+1]
        current_words_data = stats.get(current_word, dict())
        # tallennetaan tieto, että mikä oli seuraava sana
        old_count = current_words_data.get(next_word, 0)
        current_words_data[next_word] = old_count + 1
        stats[current_word] = current_words_data
    #
    # lasketaan seuraavien sanojen esiintymistodennäköisyys
    # jokaiselle sanalle erikseen
    if False:  # skipataan, koska Skulptissa ei ole random.choices()
        for word, next_words in stats.items():
            N = len(next_words)
            word_probs = dict()
            for next_word in next_words:
                word_probs[next_word] = 1.0 * next_words[next_word] / N
            stats[word] = word_probs
    return stats


def kaunista_runo(poem):
    u"""Kaunistetaan tuotetun runon ulkoasu"""
    res = ''
    first = True
    # Markkeri isoille kirjaimille:
    got_dot = False
    # Jokainen sana käsitellään
    for word in poem:
        if first:
            word = word.capitalize()
            first = False
        elif got_dot:
            word = word.capitalize()
            got_dot = False
        elif word == ',':
            word = ',\n'
        elif word == '.':
            word = '.\n'
            got_dot = True
        elif word == '!':
            word = '!\n'
            got_dot = True
        res += word + ' '
    return res


def luo_runo(text_stats, plength=20):
    u"""Luo runon Markov Chain statistiikan pohjalta"""
    ## Valitaan satunnainen aloitussana kaikkien sanojen joukosta
    curword = random.choice([x for x in text_stats.keys()])

    ## Luodaan lista, johon runon sanat sullotaan
    poem = list()
    poem.append(curword)  # Lisätään ensimmäinen sana
    for i in range(0, plength):
        ## Loput sanat arvotaan statistiikan perusteella
        #print(curword)
        try:
            nwords = text_stats[curword]
        except KeyError:
          ## Joitain sanoja ei seuraa mikään.
          ## Silloin lopetamme for-looppin tähän.
          break
        words = [x for x in nwords.keys()]
        weights = [x for x in nwords.values()]
        ## random.choiches puuttuu Skulptista :(
        # curword = random.choices(words, weights=weights, k=1)[0]
        curword = random.choice(
            [k for k in nwords for _ in range(nwords[k])])
        poem.append(curword)
    return poem



## Kutsutaan metodia, joka laskee sanojen statistiikkaa
## ja luo "Markov Chain" statistiikan.
kale_clean = clean_up(kale_txt)
text_stats = do_stats(kale_clean)

## text_stats on dictionary-tyyppinen otus.
## Sen rakennetta voisi tutkia:
##
## Tästä voi tulla aika iso tulostus
## Koska KOKO Kalevala!
#print text_stats
## Osaatko tutkia dict-datastruktuuria?

import random

## Luodaan uusi runo:

#rumaruno = luo_runo(text_stats)
#print rumaruno
#print kaunista_runo(rumaruno)
