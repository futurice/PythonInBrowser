##### FILE #####
# perimeter.py
# Perimeter of a polygon

import turtle

##### INFO #####
# Perimeter is the distance the turtle travels when it draws a closed
# polygon.

# A helper function that moves the turtle to the location (x, y) but
# does not draw a line.
def move_turtle_to(t, x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  return t

# A function that draws a square and returns its perimeter.
#
# Parameter t is a turtle.
# Parameter side is a number that tells how long a side of the square is.
def square(t, side):
  distance = 0
  for i in range(4):
    distance = distance + side
    
    t.forward(side)
    t.right(90)
  
  return distance

# Let's use the square function to draw a square with 100 steps long
# sides and print the perimeter of the square.
t = turtle.Turtle()

move_turtle_to(t, -50, 150)
square_perimeter = square(t, 100)
print "Square's perimeter: " + str(square_perimeter)

##### EXERCISES #####

##### EXERCISE 1 #####
# Complete the following function so that it draws a star. Each side
# of should be equally long, and the parameter side should determine
# the length of a side.
#
# The return value of the function should be the perimeter.

def star(t, side):
  distance = 0
  
  distance = distance + side
  t.forward(side)
  
  t.right(120)
  distance = distance + side
  t.forward(side)
  
  t.left(60)
  distance = distance + side
  t.forward(side)

  t.right(120)
  distance = distance + side
  t.forward(side)
  
  t.left(60)
  distance = distance + side
  t.forward(side)
  
  t.right(120)
  distance = distance + side
  t.forward(side)

  t.left(60)
  distance = distance + side
  t.forward(side)


  # FILL IN HERE

  # Remember to add the travelled distance to the distance variable
  # every time you move the turtle forward.
  #
  # Hint: you can avoid repetition by using a for loop.


  return distance

move_turtle_to(t, -50, 0)
star_perimeter = star(t, 100)

print "Star's perimeter: " + str(star_perimeter)

##### EXERCISE 2 #####
# How long the side of the star should be to make the perimeter of the
# square and the star equal?
#
# Either try out different lengths for the star's side (the second
# parameter in the star() function) or figure out the correct answer
# by pen and paper.
