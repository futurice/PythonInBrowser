# Jakolaskuja ja muuta matematiikkaa

##### EXERCISE #####
#
# 1. Aikaisemmassa tehtävässä huomasimme, että jakolaskut
# toimivat hieman odottamattomalla tavalla Pythonissa.
# Kokeile uudelleen mitä tulee tulokseksi tästä
# jakolaskusta:

print 1/2

# Outo tulos johtuu siitä, että jos jaettava ja jakaja ovat
# kokonaislukuja, niin Python palauttaa jakolaskusta vain
# tuloksen kokonaislukuosan. Testaa tätä vaihtamalla lukuja
# jakolaskussa, esimerkiksi 2/2, 3/2 ja 4/2.

# 2. Python osaa laskea jakolaskuja myös desimaaliluvuilla,
# jos joko jaettava tai jakaja on annettu vähintään yhden
# desimaalin tarkkuudella. Pythonissa kokonaislukuosa ja
# desimaaliosa erotellaan toisistaan pisteellä, ei siis
# pilkulla niin kuin suomen kielessä. Esimerkiksi 2.0 tai
# 2.5. Kokeile seuraavia jakolaskuja poistamalla #-merkki ja
# välilyönti rivin alusta:

# print 1.0/2.0
# print 2.5/5
# print 5/3.0

# 3. Keksitkö mitä seuraava laskuoperaattori tekee? Vihje:
# kokeile eri luvuilla.

# print 3.0 ** 2.0

# 4. Entäs tämä? Vihje: Tämä liittyy jakolaskuun. Kokeile
# vaihtaa ensimmäisen luvun paikalle eri numeroita ykkösestä
# etenpäin.

# print 4.0 % 3.0

# 5. Lisää matemaattisia operaattoreita löytyy
# math-kirjastosta. Kirjaston saa ladattua käyttöön, jos
# poistat seuraavalta riviltä #-merkin.

# import math

# Import-lause tarvitsee olla koodissa vain yhden kerran.
# "Importtauksen" jälkeen kirjaston funktioita voi käyttää
# koodissa.
#
# Kirjastosta löytyy esimerkiksi neliöjuuri (sqrt on lyhenne
# englannin sanoista square root eli neliöjuuri):

# print math.sqrt(9)

# Kirjastosta löytyy myös pi, sini, kosini ja paljon muita
# funktioita. Katso lista kaikista saatavilla olevista
# funktioista: https://docs.python.org/3/library/math.html

# print math.pi
# print math.sin(0.0)
# print math.cos(0.0)
