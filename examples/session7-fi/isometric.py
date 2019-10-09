# Rakennetaan palikoilla

##### INFO #####
import turtle2


# Sekoittaa kaksi väriä ja palauttaa niiden yhdistelmän.
# Värit pitää antaa kolmikkona (punainen, vihreä, sininen) esim. (255, 0, 0)
# Painot kertovat kuinka paljon väriä painotetaan
def sekoita_varit(vari1, vari2, paino1=1.0, paino2=1.0):
  u = paino1 / (paino1 + paino2)
  v = paino2 / (paino1 + paino2)
  return (u * vari1[0] + v * vari2[0],
          u * vari1[1] + v * vari2[1],
          u * vari1[2] + v * vari2[2])

# Tämä piirtää isometrisen kuution
#
# x ja y ovat kuution "ala" kärjen koordinaatit
#
# vari on kuurion väri. Se annetaan kolmikkona (punainen, vihreä, sininen),
# jossa jokainen arvo on välillä 0-255
#
# koko on kuution sivun koko
def piirra_kuutio(x, y, vari=(255, 0, 0), koko=30):
    turtle2.pauseDrawing()
    t = turtle2.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()

    # Oikea puoli
    t.fillcolor(sekoita_varit(vari, (0, 0, 0)))
    t.begin_fill()
    t.forward(koko)
    t.right(60)
    t.forward(koko)
    t.right(120)
    t.forward(koko)
    t.right(60)
    t.forward(koko)
    t.end_fill()

    # Vasen puoli
    t.fillcolor(sekoita_varit(vari, (0, 0, 0), paino1=3.0))
    t.begin_fill()
    t.right(60)
    t.forward(koko)
    t.right(60)
    t.forward(koko)
    t.right(120)
    t.forward(koko)
    t.end_fill()

    # Yläpuoli
    t.fillcolor(vari)
    t.begin_fill()
    t.right(180)
    t.forward(koko)
    t.right(120)
    t.forward(koko)
    t.right(60)
    t.forward(koko)
    t.end_fill()

    turtle2.unpauseDrawing()


##### TEHTÄVÄ 1 #####
#
# Piirretään kaksi kuutiota

piirra_kuutio(x=50, y=-100, vari=(255, 128, 64))
piirra_kuutio(x=0, y=-200, vari=(128, 16, 192))

# Siirrä kuutiot päällekkäin pinoon muuttamalla
# ylhäällä olevan funktiokutsun parametreja x ja y
#
# Ota huomioon että alempi kuutio pitää piirtää ensin,
# että ylempi kuutio peittää sen yläosan
#
# Kokeile vaihtaa kuutioiden väriä


##### TEHTÄVÄ 2 #####
#
# Lisää nyt uusia kuutioita ensimmäisen kuution viereen
#
# Jotta saat kuution piirrettyä toisen viereen, eteen tai taakse,
# pitää selvittää oikeat koordinaatit. Tee funtio, joka laskee
# oikeat koordinaatit
#
# Kun olet tehnyt funktion, voit rakennella palikoista muotoja
