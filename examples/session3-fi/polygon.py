# Piirretään monikumioita funktioilla

import turtle
t = turtle.Turtle()

##### INFO #####

# Alla on funktio, joka piirtää kolmion.
# Sillä on yksi parametri 'sivu'.
# Muuttuja 'sivu' määrittää kolmion sivun pituuden.
# Lue seuraava koodi ja selitä ystävällesi mitä se tekee

def kolmio(sivu):
  for i in range(0, 3):
    t.forward(sivu)
    t.right(120)

##### TEHTÄVÄ #####

# 1. Piirretään kolmioita: Kutsu funktiota kolmio eri sivu-parametrin arvoilla


# 2. Tee nyt funktio nimeltä nelio, joka piirtää neliön. Käytä kolmio-funktiota apuna.
# Kuinka paljon tulee nyt kääntyä forward funktion jälkeen?
# Kokeile uutta funktiotasi eri sivun arvoilla

# def nelio(sivu):
  # kirjoita koodisi tähän

# 3. Piirretään nyt viisikulmio! Tee funktio joka piirtää viisikulmion ja kokeile sitä.

# 4. Piirretään monikulmio!
# Osaatko tehdä funktion, joka piirtää minkä tahansa tasasivuisen monikulmion?
# Katso funtioita kolmio, nelio ja viisikulmio, mitä yhteistä huomaan?