# Tutustutaan kilpikonnaan

##### INFO #####
#
# Piirretäänpä jotain ruudulle. Kutsutaan avuksi kilpikonna
# nimeltä Kalle seuraavilla kolmella komennolla. Näiden
# komentojen merkitykseen perehtydään tarkemmin myöhemmissä
# tehtävissä.

import turtle
kalle = turtle.Turtle()
kalle.shape("turtle")

##### TEHTÄVÄ #####
#
# Voit komentaa kilpikonnaa liikkumaan ruudulla. Kilpikonna
# jättää ruudulle jäljen sinne missä se liikkuu.
#
# Alla kilpikonnaa käsketään kulkemaan 100 askelta eteenpäin
# (forward tarkoittaa eteenpäin englanniksi), kääntymään
# vasemmalla 90 astetta (left tarkoitta vasemmalla
# englanniksi, oikealle olisi right) ja lopuksi taas
# eteenpäin 50 askelta.

kalle.forward(100)
kalle.left(90)
kalle.forward(50)

# Paina Run-nappia ja katso mitä tapahtuu.
#
# Liikuta kilpikonnaa ympäriinsä. Tee ainakin kolme
# käännöstä ja eteenpäin siirtymää.
