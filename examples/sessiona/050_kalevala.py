## Kalevala

## Idea luonnollisen tekstin käsittelystä (LTK, aka NLP).
## Tutkitaan Kalevalan tekstiä Pythonilla.
## Kalevala tiedostoina (latin-1):
## http://www.sci.fi/~alboin/trokeemankeli/kalevalamitta-aineistoja.htm



## Ladataan Kalevalan teksti
# TODO: make it available (public/data/kal...)


## Ladattu teksti on "lista" (list) stringejä.


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

def word_stats(kale_txt):
    """Lasketaan sanojen statistiikkaa"""
    fixed_kale = list()
    # fiksaillaan ja uudelleen muotoillaan tekstiä
    for line in kale_txt:
        _ = (fixed_kale.append(
                line
                .lower()
                .replace('--', '')
                .replace('"', '')
                .replace(';', '')
                .replace('\n', ' \n')
                .replace(',', ' ,')
                .replace('.', ' .')
                .replace('?', ' ?')
                .replace('!', ' !')
        ))
    # laitetaan kaikki sanat yhteen pötköön
    words = list()
    for line in fixed_kale:
        for word in line.split():
            words.append(word)
    print(len(words), 'words after splitting.')
    #print(words)

    stats = dict()
    # käydään läpi kaikki sanat
    for n in range(0, len(words)-1):
        current_word = words[n]
        next_word =words[n+1]
        current_words_data = stats.get(current_word, dict())
        # tallennetaan tieto, että mikä oli seuraava sana
        old_count = current_words_data.get(next_word, 0)
        current_words_data[next_word] = old_count + 1
        stats[current_word] = current_words_data

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
    """Kaunistetaan tuotetun runon ulkoasu"""
    res = ''
    first = True
    got_dot = False
    for item in poem:
        if first:
            item = item.capitalize()
            first = False
        elif got_dot:
            item = item.capitalize()
            got_dot = False
        elif item == ',':
            item = ',\n'
        elif item == '.':
            item = '.\n'
            got_dot = True
        elif item == '!':
            item = '!\n'
            got_dot = True

        res += item + ' '
    return res


def luo_runo(text_stats):
    """Luo runon Markov Chain statistiikan pohjalta"""
    ## Valitaan satunnainen aloitussana kaikkien sanojen joukosta
    curword = random.choice([x for x in text_stats.keys()])

    ## Luodaan lista, johon runon sanat sullotaan
    poem = list()
    poem.append(curword)  # Lisätään ensimmäinen sana
    for i in range(0, 20):
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
        curword = random.choice([k for k in nwords for _ in range(nwords[k])])
        poem.append(curword)
    return poem



## Kutsutaan metodia, joka laskee sanojen statistiikkaa
## ja luo "Markov Chain" statistiikan.
text_stats = word_stats(kale_txt)

## text_stats on dictionary-tyyppinen otus.
## Sen rakennetta voisi tutkia -> TODO: tutustuminen dict-tyyppiin.

#print(text_stats)

import random  ## TODO: tutustuminen random -kirjastoon

## Tämä rivi luo uuden runon.
#print(kaunista_runo(luo_runo(text_stats)))
