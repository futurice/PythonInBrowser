# Let's draw a flower

import turtle
t = turtle.Turtle()

##### INFO #####
# Firstly, let's make the drawing a bit faster.
# It's possible to adjust the speed of the turtle with commad 'speed(0)'
t.speed(0)

# We can set the background color.
turtle.Screen().bgcolor("lightgreen")

# The line color can be changed, too.
t.color("red")

##### EXERCISE #####
# Let's draw something that perhaps resembles a flower
# It's handy to use a for loop for that.

petalwidth = 50 # add / change here any number between 10 and 200
direction1 = 181 # you can modify these later, but now leave them with values 181
direction2 = 178 # and 178

for i in range (100):
  # Let's start with going forward the amount of petalwidth
  # and add the value of the iterator.
  # That will give us nice shape for the petals
  t.forward(petalwidth + i)
  # Let's turn back
  t.left(direction1)
  # and draw the same length
  t.forward(petalwidth + i)
  # The for loop now repeats this drawing 100 times.

# Click 'Run' and see what happens.

# It's possible to change the color of drawing in the middle of code
# Enable the code on the next line by removing the comment character
# '#' and the space from the beginning of the next line. Removing the
# comment character is called uncommenting.
# t.color("green")

# Then uncomment the following lines.
# These draw a similar pattern as the first loop
# but this time with different color and turning to direction2.

# for i in range (0, 100):
#   t.forward(petalwidth+i)
#   t.left(direction2)
#   t.forward(petalwidth + i)

# Click again 'Run' and see what kind of flower is going to appear.

# Then uncomment all the following lines and see what kind of flower there is.

# t.color("blue")

# for i in range (0, 100):
#   t.forward(petalwidth+i)
#   t.left(direction1)
#   t.forward(petalwidth + i)

# t.color("pink")

# for i in range (0, 100):
#   t.forward(petalwidth + i)
#   t.left(direction1)
#   t.forward(petalwidth + i)

# t.color("orange")

# for i in range (0, 100):
#   t.forward(petalwidth+i)
#   t.left(direction1)
#   t.forward(petalwidth + i)

# t.color("yellow")

# for i in range (0, 100):
#   t.forward(petalwidth + i)
#   t.left(direction2)
#   t.forward(petalwidth + i)

# When you've drawn the first version of the flower
# feel free to change the values of petalwidth and direction1 and direction2.
# and see how they affect the drawing.
