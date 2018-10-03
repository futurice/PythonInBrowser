# Käydään läpi mitä opimme viime viikolla (ja myös jotakin uutta)
# Jos jokin asia mietityttää, kysy vain rohkeasti apua!

##### INFO #####
# Viime viikon tärkeimmät asiat olivat:
# 1. print-komento
# 2. muuttujan käyttö
# 3. kilpikonnan käyttäminen piirtämiseen

# Ohelmointi vaatii usein tiedon etsimistä muista lähteistä
# ja uuden tiedon soveltamista omaan ohjelmaasi.
# Käytännössä tietoa ohjelmoinnista löytää hyvin Internetistä.
# Käytä viime viikon tehtäviä lähteenä tehdessäsi seuraavia tehtäviä

##### TEHTÄVÄT #####

##### TEHTÄVÄ 1 #####
# 1. kirjoita koodinpätkä joka printtaa kaksi riviä
# Ensimmäisellä rivillä tulee olla teksti:
# "Minun lempivärini on 'lempivärisi'"
# Toisella rivillä pitää olla yhtälö joka laskee
# kuukauden jäljellä olevat päivät
# VINKKI: tarkista tietokoneelta kuinka monesko päivä tänään on ja kuinka monta päivää tässä kuussa on.
# Printtauksen tulee sisältää vain yksi numero: yhtälön ratkaisu

# <------ kirjoita koodisi tähän (ja klikkaa 'Run' printataksesi)------->

##### TEHTÄVÄ 2 #####
# Yhtenä päivänä lempivärisi saattaa olla vihreä ja toisena oranssi.
# Luo muuttuja nimeltä lempivari ja anna sille arvoksi lempivärisi

# <------  kirjoita muuttuja tähän ------->

# Kirjoita sitten koodi joka printtaa tekstin "Lempivärini in 'lempivärisi'"
# Käytä tällä kertaa muuttujaa lempivari ilmaisemaan lempivärisi

# <------ kirjoita koodisi tähän (ja klikkaa 'Run' printataksesi)------->

# Tarkistuksena muuta lempiVari muuttujan arvoa ja klikkaa 'Run'
# tarkista että lempiväri on muuttunut printtauksessa

##### TEHTÄVÄ 3 #####
# Pystyäksemme piirtämään viereiselle piirtoalueelle, meidän täytyy käyttää kilpikonnaa
# Tätä varten meidän tulee tuoda (importtaa) kilpikonna ja asettaa se muuttujaan.

# <------ Tuo (import) kilpikonna tässä ------->
# näin: import turtle
# <------ aseta kilpikonna muuttujaan 'jane', muistatko? ------>

# Piirrä seuraava kuvia
#
# eteenpäin 50 pikseliä, käännä 135 astetta oikealle
# eteenpäin 100 pikseliä, käännä 135 astetta oikealle, eteenpäin 100 pikseliä,
# käännä 135 astetta oikealla ja siirrä 50 pikseliä eteenpäin.
#
# Pystytkö arvaamaan minkä kuvion kilpikonna piirtää?

# <------ kirjoita koodisi tähän ------->

# On mahdollista piirtää myös muilla väreillä. Musta on vain oletusväri.
# Kilpikonnan värin voi muuttaa lisäämällä seuraavan rivin ennen piirtämistä:
# jane.color("pink")

# Voit myös käyttää muuttujaa määrittääksesi piirroksen värin.
# Muuta muuttujan lempivari arvo englanniksi esim. "green" (vihreä), "blue" (sininen) tai "yellow" (keltainen)
# ja korvaa väriä vaihtava koodi seuraavalla rivillä
#
# jane.color(lempivari)
#
# Muista että käyttäessäsi muuttujia et tarvitse lainausmerkkejä

# Onnittelut! Olet käynyt läpi viime viikon tärkeimmät asiat
# ja oppinut piirtämään eri väreillä

##### LISÄTEHTÄVÄT #####

# Mikä olisi helpoin tapa piirtää kolmio loppuun?
# Muuta muuttujan lempivari arvoa ja kokeile että se toimii.
# Miten voisit piirtää toisen kolmion eri suuntaan ja eri värillä
