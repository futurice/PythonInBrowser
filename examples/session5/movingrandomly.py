import turtle
import random
t = turtle.Turtle()
colors = ["green", "blue", "red", "yellow", "pink"]

##### EXERCISES #####
# Below you can see function called doMove.
# Currently the function does only two things. It move the turtle forward 10 steps.
# Go ahead and try it!
#
# After this exercise we'd like the function go to random direction, random pixels and with random color.
# Let's do this step by step.
#
# It's maybe good to remember how to use random:
# random.randint(0, 10) gives random int from range 0 to 10
# random.choice(someSet) gives random element of someSet

##### EXERCISE 1 #####
# Let's make the lenght of going forward random.
# Override the value 10 of step with random value from range 10 to 100

##### EXERCISE 2 #####
# Let's make the angle random.
# Override the value 0 of angle with random value from range 0 to 180
# Also remember to change the angle with command t.right(angle)

##### EXERCISE 3 #####
# Let's make the color random.
# Override the value "black" of color with random choice from set colors
# Also remember to change the color with command t.color(color)

# Modify this function
def doMove():
  angle = 0
  step = 10
  color = "black"
  t.forward(step)

# To see how the doMove() function controls turtle's movement, let's
# call the function. Each call moves the turtle one step forward. To
# make the turtle move continue moving, we call the function
# repeatedly inside a loop. "while True" means that we continue
# calling the function forever.
while True:
  doMove()

##### EXERCISE 4 #####
# Did your Turtle dissappear?
# How could we prevent that?
# Let's look into this next.
