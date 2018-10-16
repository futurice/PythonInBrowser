# Opetetaan kilpikonna piirtämään tähtiä!

import turtle
t = turtle.Turtle()

##### INFO #####
#
# Tutustuimme tähden piirtämiseen jo aikaisemmassa
# tehtävässä. Komennot ovat alla muistin virkistykseksi.
#
# Tähden piirtäminen vaatii monta vaihetta. Entä jos haluamme
# piirtää monta tähteä? Tarvitseeko kaikki vaiheet toistaa
# uudelleen? Onneksi ei! Annamme tähden piirtävälle joukolle
# komentoja nimen käytämme sitä uudelleen.
#
# Ohjelmoinnissa nimettyä joukkoa komentoja kutsutaan funktioksi.

# Seuraava koodinpätkä määrittelee uuden funtion.
#
# "tahti()" on nimi jonka annamme funktiolle. Nimi voi olla 
# mitä vain kunhan se loppuu sulkuihin ()

def tahti():
  # "tahti()" on lyhennetty muoto seuraaville komennoille.
  # Kaikki "def" avainsanan jälkeen sisennetty koodi on osa 
  # funktiota.
  t.forward(50)
  t.left(160)
  t.forward(50)
  t.right(70)
  t.forward(50)
  t.left(160)
  t.forward(50)
  t.right(70)
  t.forward(50)
  t.left(160)
  t.forward(50)
  t.right(70)
  t.forward(50)
  t.left(160)
  t.forward(50)
  t.right(70)

# Funktio ei itsessään tee vielä mitään. Funktion koodi ajetaan
# vasta kun funtiota kutsutaan nimeltä. Voit testata että mitään
# ei tapahdu kun painat run.

##### TEHTÄVÄ 1 #####
#
# Voit nyt ajaa tähden piirtämiseen vaadittavat komennot
# kutsumalla funktion nimeä.

# Poista kommentti seuraavalta riviltä ja paina run
# niin näet mitä funktio tekee.

# tahti()

##### TEHTÄVÄ 2 #####
#
# Piirretään tähtiä! "t.goto" siirtää kilpikonnaa uuteen
# paikkaan ja "tahti()" piirtää tähden. Poista kommentit
# seuraavilta riveiltä.

# t.penup()
# t.goto(80, -40)
# t.pendown()
# tahti()

# Piirrä vielä kaksi tähteä lisää haluamaasi paikkaan käyttäen
# edellistä kaavaa kilpikonnan liikutteluun.

#####
# TEHTÄVÄ 3 #####
#
# Tähän mennessä kaikki tähdet ovat ollet saman kokoisia, koska
# tähden sivun pituus on määritelty olemaan 50 pikseliä kohdassa
# "t.forward(50)"
#
# Entä jos haluamme pirtää erikokoisia tähtiä? Voimme korvata
# sivunpituuden 50 muuttujalla ja antaa halutun pituuden funktiolle
# sitä kutsuttaessa.
#
# Alla on uusi funktio. Se on muuten sama kuin tahti() -funktio,
# mutta tähden sivun pituus on korvattu muuttujalla "koko".
# Huomaa että muuttuja koko annetaan funktion sulkeiden sisällä.
# Funktiolle annettavaa muuttujaa kututaan myös parametriksi.
# Tämä tarkoittaa että muuttujan "koko" todellinen arvo
# määritellään vasta funktiota kutsuttessa.

def tahti_koolla(koko):
  t.forward(koko)
  t.left(160)
  t.forward(koko)
  t.right(70)
  t.forward(koko)
  t.left(160)
  t.forward(koko)
  t.right(70)
  t.forward(koko)
  t.left(160)
  t.forward(koko)
  t.right(70)
  t.forward(koko)
  t.left(160)
  t.forward(koko)
  t.right(70)


# Funtiolle tahti_koolla annettaan muuttujan koko arvo parametrina
# funktiota kutsuttaessa. Käytännössä tämä tapahtuu lisäämällä parametrin
# koko arvo funktion kutsun sulkeiden sisään.

# Esimerkiksi kutsu "tahti_koolla(10)" piirtää pienen tähden, koska
# jokaisessa "t.forward(koko)" kutsussa koko korvataan nyt 10:llä.

# Huomaa että nyt funktiolle on pakko antaa jokin arvo sulkeiden
# sisällä. Muuten funtio ei tiedä mikä muuttujan koko arvo on ja
# koodi aiheuttaa virheen.

# Poista kommentit seuraavilta riveiltä piirtääksesi pienen tähden.

# t.penup()
# t.goto(-80, 100)
# t.pendown()
# tahti_koolla(20)

# Piirrä seuraavaksi
# pieni tähti (koko = 12),
# keskikokoinen tähti (koko=25)
# ja jättitähti (koko=100)
# Haluamiisi paikkoihin
