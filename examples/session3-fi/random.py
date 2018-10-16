# Tällä kertaa opimme miten saamme tietokeoneelta satunnaisia arvoja

##### INFO #####
# Importataan random -kirjasto, jolla saamme koodin antamaan meille
# satunnaisia lukuja.
# Käytämme myöhemmin satunnaisia lukuja piirtämiseen.
import random

# Voit printata satunnaisen desimaalin 0 ja 1 väliltä
print u"Desimaali 0-1 väliltä: "
print random.random()  # Random float x, 0.0 <= x < 1.0

# On myös hyödyllistä saada satunnaisia kokonaislukuja
# Tämä saadaan aikaan kutsumalla funktiota randint
print u"Kokonaisluku (integer) 1-10:"
print random.randint(1, 10)  # Kokonaisluku väliltä 1-10

# Voit saada myös satunnaisen desimaaliluvun halutulta väliltä
print u"Desimaali 1-10 väliltä:"
print random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0

# Seuraava funtio palauttaa satunnaisen kokonaisluvun, joka on
# jaollinen kolmannella parametrilla
print u"Parillinen luku väliltä 1-100:"
print random.randrange(0, 101, 2)
print u"7 jaollinen luku väliltä 0-98:"
print random.randrange(0, 101, 7)  # integer divisible by 7 – from 0 to 98

# Voit myös saada satunnaisia kirjaimia merkkijonosta (string)
print u"Satunnainen kirjain:"
print random.choice('abcdefghij')  # Valitse satunnainen elementti

# Voit myös sekoittaa listan numeroita
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print u"Sekoitettu lista"
print items

##### TEHTÄVÄ #####
# Klikkaa 'Run' ja katso tulokset
# Kikkaa uudellen 'Run' ja katso mitä tapahtuu

# Huomaatko, että jokaisella kerralla saat eri tulokset?

# Kokeile muuttaa parametrien arvoja.
# Pystytkö päättelemään mitä jokainen parametri tekee?