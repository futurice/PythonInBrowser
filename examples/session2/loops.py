# Loops

##### INFO #####
#
# Sometimes drawing a complex shape requires repeating same
# commands several times. You can use a loop to repeat a
# block of commands.

import turtle
t = turtle.Turtle()

# The following is an example of a loop.
#
# "for" means tells the computer to repeat something
# multiple times.
#
# "in range(2)" tells that we repeat the commands two times.
#
# "i" is a variable that gets increased on every iteration.
# It is not used in this exercise but later on we will see
# examples where is is useful.

for i in range(2):
  # The following lines are the commands that are repeated.
  # These lines are indented, that is they start with two
  # spaces, because the indentation tells which lines belong
  # to the block of commands that are repeated.
  t.forward(30)
  t.left(120)
  t.forward(30)
  t.right(60)

##### EXERCISE 1 #####
#
# Press 'run' to see what happens.
#
# How many times does does the loop need to be repeated to
# complete the star shape? Put the correct value inside the
# parenthesis in the range(...) expression. Hint: It might
# be easier to guess and try out different values than to
# deduce the correct answer.

##### EXERCISE 2 #####
#
# Think of other shapes that have a repeating pattern.
# Examples: square, staircase, waves.
#
# Modify the loop to draw the shape you selected.
#
# Hint: Start by drawing only one repetition by writing
# "range(1)" and get it drawn correctly. Then you can repeat
# the shape as many times as you like by changing the range
# value.
