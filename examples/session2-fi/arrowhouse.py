# Harjoitellaan arkkitehtuuria ja piirretään talo

##### INFO #####
# Importtaa, eli tuo näkyviin, kilpikonnan (turtle) ja asettaa sen muuttujaan ’t’.
import turtle
t = turtle.Turtle()

# Saatat jo muistaa että että voimme käyttää kilpikonnaa piirtämiseen.
# Seuraavaksi määrittelemme talon seinän (wall) pituuden.
# Jotta saamme katon sopivan pituiseksi, käytetään suhdetta 1:5.
# Asetetaan tämä muuttujaan 'gutter'.

wall = 50
gutter = wall / 5

# Siirrämme ensin kilpikonnaa eteenpäin seinän pituuden verran,
# käännämme sen 90 astetta ja siirrämme sitä taas eteenpäin seinän pituuden verran
# sitten käännämme sen 90 astetta oikealle, siirrämme eteenpäin muuttujan gutter verran.
# gutter on yksi viidesosa seinän pituinen.
# Käännämme vasemmalle 135 astetta ja siirrämme eteenpäin taas seinän pituuden.

t.forward(wall)
t.left(90)
t.forward(wall)
t.right(90)
t.forward(gutter)
t.left(135)
t.forward(wall)

##### TEHTÄVÄ #####
# Klikkaa 'run' ja katso mitä tapahtuu.
# Piirtoalueelle on on piirretty puolikas talo.
# Viimeistele talo lisäämällä sopivat kilpikonnan komennot ylös,
# edellisten komentojen perään.
# VINKKI: tarvitset 6 riviä lisää talon viimeistelemiseksi.
# Voit aina klikata 'run' ja
# testata kulkeeko kilpikonna oikeaan suuntaan.
# VINKKI: On järkevää käyttää muutujia 'wall' ja 'gutter' eteenpäin komennoissa

# Kun talo on valmis, saatat miettiä
# näyttääkö se enemmän talolta vai nuolelta.
# Mutta tämä on varmaan makukysymys.

# Käyttäessäsi gutter muuttujan arvona suhdetta wall muuttujaan,
# saat sen hyödyn että talo on helppo piirtää eri kokoisena.
# Muuta muuttujan wall arvo numeroksi 10 ja 150 välillä
# ja tarkista että piirrustus toimii yhä.

# Viimeisenä kokeile muuttaa wall arvo 500:ksi ja klikkaa 'Run'.
# Odota hetki että kilpikonna palaa näytölle.
# Huomaat että linjat eivät kohtaa täydellisesti. 1:5 suhde ei ole täydellinen.

# Voit kysyä matematiikan opettajaltasi mistä tämä johtuu.
# Mikä olisi oikea tapa laskea muuttujan gutter arvo?
