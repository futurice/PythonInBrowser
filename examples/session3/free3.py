# Let's draw with random colors

##### INFO #####
# Use all the concepts that you've learnt so far
# and draw something on the canvas.

# Here is a starting point for drawing,
# using random, for loop and a function.

import turtle  # remember, we need turtle everytime we want to draw

import random  # random needs to be imported, too

t = turtle.Turtle()
t.speed("fastest")

# Let's modify the background color of the canvas
# We can set the color like this:
turtle.Screen().bgcolor("black")

# Let's draw with multiple colors.
# It's possible to define our color palette in an array
colors = ["red", "blue", "green", "yellow", "orange", "brown", "purple", "pink"]

# Then we can pick our with index number of the array
colorFromPalette = colors[0] # Now color from palette is red

# The real fun comes when we pick color randomly
# Let's first define, what is the index of the last color in the color palette
# We can do it with a variable
lastColor = len(colors) - 1

# Random color can be chosen like this. It can be stored in a variable.
randomColor = colors[random.randint(0, lastColor)]

##### TEHTÄVÄ #####
# Comment line 23: screen.bgcolor("black")
# and uncomment the following line
# turtle.Screen().bgcolor(randomColor)

# Let's define a function, that draws squares, but with changing angle
# – so that it actually draws a circle. Let's also change the drawing color
# after drawing each square and name it colorfulOlympicCircle

##### THIS BLOCK IS A FUNCTION #####
def colorfulOlympicCircle():
  t.forward(80);
  t.left(92);
  newColor = colors[random.randint(0, len(colors) - 1)]
  t.color(newColor)
##### UNTIL HERE #####

# The code above is just defining a function, it doesn't actually do anything.
# Let's use that function to draw.

t.penup()
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

# Let's learn a new thing: nested for loop.
# The example below repeats 5 times the drawing of the function we defined earlier.

# This part is the outer loop, which is repeated 5 times
for i in range(5):
  # This is the for loop inside the outer loop. It gets repeated 100 times.
  for i in range(100):
    colorfulOlympicCircle()
  # This part again belongs to the outer for loop
  t.penup()
  t.left(90)
  t.forward(200)
  t.pendown()

# Try adding the following line as the last line of the function.
# turtle.Screen().bgcolor(newColor)
# Remember to check that the indentation is correct.

# Then go on and modify the code as you wish, adding more circles, changing its
# shape and the colors. And so on.

