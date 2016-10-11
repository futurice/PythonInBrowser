# Let's teach the turtle to draw stars!

import turtle
t = turtle.Turtle()

##### INFO #####
#
# We already know how to draw a star from an earlier
# exercise (and the commands to do it are shown below if you
# don't remember how it was done).
#
# Drawing a star requires a quite many steps. Do we need to
# repeat all the steps if we want to draw a second star?
# Luckily no, because we can give a short name to a sequence
# of commands and refer to them using just the short name.
#
# In programming, a sequence of commands with a name is
# called a function.

# The following defines a new function.
#
# "def" tells that this is a function.
#
# "star()" is the name we give to the function. It can be
# anything we like as long as it ends in ().

def star():
  # The "star()" is a short name for the following commands.
  # Everything after the "def" line indented with two spaces
  # will be part of the function.
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

# The above just defines what the function should do when it
# is executed. It doesn't draw anything yet. You can confirm
# this by pressing "run" now. No star will be drawn.

##### EXERCISE 1 #####
#
# We can execute the above long sequence of commands by
# simply writing the function's name. This is known as
# "calling the function" or "executing the function".

# To see what the function does, uncomment the next line and
# press run.

# star()

##### EXERCISE 2 #####
#
# Draw some more stars! "t.goto" moves the turtle to a new
# location and "star()" draws a star. Uncomment the
# following lines.

# t.penup()
# t.goto(80, -40)
# t.pendown()
# star()

# Draw two more stars at the location you choose using the
# above pattern to move the turtle.

##### EXERCISE 3 #####
#
# So far, all stars are the same size because the length of
# the star's side is determined to be 50 pixels by
# "t.forward(50)" in the function's definition above.
#
# What if we want to draw bigger and smaller stars? We can
# replace the number 50 with a variable and give the actual
# size only when calling the function.
#
# Below is a second function. It is otherwise identical to
# the star() function except that the length 50 has been
# replaced with a variable called "size". Notice that the
# variable size appears also on the "def" line inside the
# parenthesis. This is the way to tell the computer that the
# value for size will be supplied later when the function is
# called.

def star_with_size(size):
  t.forward(size)
  t.left(160)
  t.forward(size)
  t.right(70)
  t.forward(size)
  t.left(160)
  t.forward(size)
  t.right(70)
  t.forward(size)
  t.left(160)
  t.forward(size)
  t.right(70)
  t.forward(size)
  t.left(160)
  t.forward(size)
  t.right(70)

# The value of the size variable must be given when the
# function is called. Otherwise there will be an error
# because the function does not known how long the sides of
# the star should be.
#
# The value is supplied by putting the desired number
# between parenthesis when calling the function. For
# example, "star_with_size(10)" would draw a tiny star with
# the length of a side of just 10 pixels because "size" on
# every "t.forward(size)" in the function definition will be
# replaced by 10.

# Uncomment the following lines to draw a small star.

# t.penup()
# t.goto(-80, 100)
# t.pendown()
# star_with_size(20)

# Draw one tiny star (size = 12), one medium star (size =
# 25) and one huge star (size = 100) at locations that you
# choose.
