import turtle
import random
t = turtle.Turtle()
varit = ["green", "blue", "red", "yellow", "pink"]

##### TEHTÄVÄ #####
# Alla näet funktion nimeltä teeLiike.
# Nyt funktio tekee vain yhden asian: liikuttaa kilpikonnaa 10 askelta eteenpäin.
# Kokeile!
#
# Tämän tehtävän jälkeen haluamme että kilpikonna kulkee satunnaiseen suuntaan,
# satunnaisen määrän ja satunnaisella värillä.
# Seuraa ohjeita seuraavissa tehtävissä. Toteutamme tämän askel askeleelta.
#
# Nyt on hyvä muistella miten random eli satunnaisuus toimii:
# random.randint(0, 10) antaa satunnaisen kokonaisluvun väliltä 0-10
# random.choice(listaVaihtoehtoja) antaa sanunnaisen elementin listasta listaVaihtoehtoja

##### TEHTÄVÄ 1 #####
# Tehdään ensin kilpikonnan ottamista askelista satunnaisen pituisia.
# Vaihda askel muutujan pituus 10:stä olemaan satunnainen luku väliltä 10-100

##### TEHTÄVÄ 2 #####
# Tehdään kulmasta satunnainen.
# Vaihda kulma muuttujan arvo 0:sta satunnaiseen lukuun väliltä 0-180
# Muista myös muuttaa kilpikonnan kulmaa komennolla t.right(kulma)

##### TEHTÄVÄ 3 #####
# Tehdään muuttujasta vari satunnainen.
# Muuta arvo "black" satunnaiseksi valinnaksi listasta varit.
# Muista vaihtaa väriä komennolla t.color(vari)


# Tee muokkaukset seuraavaan funktioon
def teeLike():
  kulma = 0
  askel = 10
  vari = "black"
  t.forward(askel)

# Nähdäksemme miten teeLiike() vaikuttaa kilpikonnan liikkeisiin,
# kutsumme funktiota ikuisessa loop -silmukassa.
# (Osaatko selittää miksi seuraava silmukka jatkuu ikuisesti?)
while True:
  teeLike()

##### TEHTÄVÄ 4 #####
# Katosiko kilpikonnasi piirtoalueelta?
# Miten voisimme estää tämän?
# Tutustumme tähän seuraavaksi.
