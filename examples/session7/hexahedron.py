import turtle
t = turtle.Turtle()


##### EXERCISE 1 #####
# Fill the functions so that you can draw 3D hexahedron.
#
# The picture on this page shows an example of the shape you should
# draw: https://simple.wikipedia.org/wiki/Cuboid
#
# Note that you should use the measures given in the definition of
# hexahedron.

# Function to draw frontside, fill this
def frontside(w, h):
  print "This function should draw the front side of the hexahedron"

# Function to draw topside, fill this
def topside(w, d):
  print "This function should draw the top side of hexahedron"

# Function to draw rightside, fill this
def rightside(h, d):
  print "This function should draw the right side of hexahedron"

# Fill the function frontside, topside and rightside to make this function draw hexahedron
# Here w is width, h is height and d is depth

def hexahedron(w, h, d):
  frontside(w, h)
  topside(w, d)
  rightside(h, d)

t.penup()
t.goto(0, -200)
t.pendown()
hexahedron(50, 50, 50)


##### EXERCISE 2 #####
# After you have implemented the functions, you can draw hexahedrons
# of different size. Uncomment the following lines and see what
# happens.

#hexahedron(200, 100, 200)
#hexahedron(70, 100, 200)
