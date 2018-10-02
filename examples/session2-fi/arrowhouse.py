# Harjoitellaan arkkitehtuuria ja piirretään talo

##### INFO #####
# Importtaa, eli tuo näkyviin, kilpikonnan (turtle) ja asettaa sen muuttujaan ’t’.
import turtle
t = turtle.Turtle()

# Saatat jo muistaa että että voimme käyttää kilpikonnaa piirtämiseen.
# Seuraavaksi määrittelemme talon seinän pituuden.
# Jotta saamme katon sopivan pituiseksi, käytetään suhdetta 1:5.
# Asetetaan tämä muuttujaan 'kouru'.

seina = 50
kouru = seina / 5

# Siirrämme ensin kilpikonnaa eteenpäin seinän pituuden verran,
# käännämme sen 90 astetta ja siirrämme sitä taas eteenpäin seinän pituuden verran
# sitten käännämme sen 90 astetta oikealle, siirrämme eteenpäin muuttujan kouru verran.
# kouru on yksi viidesosa seinän pituinen.
# Käännämme vasemmalle 135 astetta ja siirrämme eteenpäin taas seinän pituuden.

t.forward(seina)
t.left(90)
t.forward(seina)
t.right(90)
t.forward(kouru)
t.left(135)
t.forward(seina)

##### TEHTÄVÄ #####
# Klikkaa 'run' ja katso mitä tapahtuu.
# Piirtoalueelle on on piirretty puolikas talo.
# Viimeistele talo lisäämällä sopivat kilpikonnan komennot ylös,
# edellisten komentojen perään.
# VINKKI: tarvitset 6 riviä lisää talon viimeistelemiseksi.
# Voit aina klikata 'run' ja
# testata kulkeeko kilpikonna oikeaan suuntaan.
# VINKKI: On järkevää käyttää muutujia 'seina' ja 'kouru' eteenpäin komennoissa

# Kun talo on valmis, saatat ihmetellä
# näyttääkö se enemmän talolta vai nuolelta.
# Mutta tämä on varmaan makukysymys.

# Käyttäessäsi kouru muuttujan arvona suhdetta seina muuttujaan,
# saat sen hyödyn että talo on helppo piirtää uudelleen eri kokoisena.
# Muuta muuttujan seina arvo numeroksi 10 ja 150 välillä
# ja tarkista että piirrustus toimii yhä.

# Viimeisenä kokeile muuttaa seina arvo 500:ksi ja klikkaa 'Run'.
# Odota hetki että kilpikonna palaa näytölle.
# Huomaat että linjat eivät kohtaa täydellisesti. 1:5 suhde ei ole täydellinen.

# Voit kysyä matematiikan opettajaltasi mistä tämä johtuu.
# Mikä olisi oikea tapa laskea muuttujan kouru arvo?
