# Piirretään kukka

import turtle
t = turtle.Turtle()

##### INFO #####
# Ensimmäiseksi, tehdään piirtämisestä nopeampaa
t.speed(0)

# Voimme asettaa taustavärin
turtle.Screen().bgcolor("lightgreen")

# Viivan värin voi myös muuttaa
t.color("red")

##### TEHTÄVÄ #####
# Piirretään jotain joka muistuttaa kukkaa

teralehdenPituus = 50 # lisää / muuta tähän mikä tahansa numero 10 ja 200 väliltä
suunta1 = 181 # voit muokata tätä myöhemmin, mutta toistaiseksi jätä arvoiksi 181
suunta2 = 178 # ja 178

# Kukka muodostuu useista vinoista viivoista. Loop-silmukkaa on
# kätevä käyttää useiden viivojen piirtämiseen eri kulmissa
for i in range(100):
  # Aloitetaan menemällä eteenpäin teralehdenPituus
  # lisättynä iteraattorin i arvo verran
  # Tällä saamme hienon muodon terälehdille
  t.forward(teralehdenPituus + i)
  # Käännytään takaisin
  t.left(suunta1)
  # piirretään taas sama pituus
  t.forward(teralehdenPituus + i)
  # Loop-silmukka toistaa piirrustuksen 100 kertaa

# Klikkaa 'Run' ja katso mitä tapahtuu

# On mahdollista muuttaa piirroksen väriä kesken koodin
# Ota käyttöön seuraavalla rivillä poistamalla kommenttimerkki
#  '#' rivien edestä
# t.color("green")

# Seuraavaksi poista kommentointi seuraavilta riveiltä.
# Nämä rivit piirtävät samankaltaisen kuvion kuin ensimmäinen loop-silmukka
# mutta tällä kertaa eri suunta2 suuntaan ja eri värillä

# for i in range (0, 100):
#   t.forward(teralehdenPituus + i)
#   t.left(suunta2)
#   t.forward(teralehdenPituus + i)

# Klikkaa taas 'Run' ja katso millainen kukka ilmestyy

# Sitten voit poistaa kommentit seuraavilta riveiltä
# ja näet millainen kukka muodostuu

# t.color("blue")

# for i in range (0, 100):
#   t.forward(teralehdenPituus + i)
#   t.left(suunta1)
#   t.forward(teralehdenPituus + i)

# t.color("pink")

# for i in range (0, 100):
#   t.forward(teralehdenPituus + i)
#   t.left(suunta1)
#   t.forward(teralehdenPituus + i)

# t.color("orange")

# for i in range (0, 100):
#   t.forward(teralehdenPituus+i)
#   t.left(suunta1)
#   t.forward(teralehdenPituus + i)

# t.color("yellow")

# for i in range (0, 100):
#   t.forward(teralehdenPituus + i)
#   t.left(suunta2)
#   t.forward(teralehdenPituus + i)

# When you've drawn the first version of the flower
# feel free to change the values of teralehdenPituus and suunta1 and suunta2.
# and see how they affect the drawing.
# Kun olet saanut kukan ensimmäisen version piirrettyä,
# muuttele vapaasti muuttujien teralehdenPituus, suunta1 ja suunta2 arvoja
# ja katso miten ne vaikuttavat piirokseen.
