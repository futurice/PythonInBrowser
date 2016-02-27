# Building with blocks

##### INFO #####
import turtle
import turtlehelpers

# Blends two colors and returns their combination.
# The colors must be given as (red, green, blue).
# The weights tell how much each color is used.
def blend_colors(color1, color2, weight1=1.0, weight2=1.0):
  u = weight1/(weight1 + weight2)
  v = weight2/(weight1 + weight2)
  return (u*color1[0] + v*color2[0],
          u*color1[1] + v*color2[1],
          u*color1[2] + v*color2[2])

# Draws an isometric cube.
#
# x and y are the coordinates of the "bottom" vertex in 2D
# coordinates.
#
# color is the color of the cube. It must be given as
# triplet of (red, green, blue) values. Each value is in the range
# from 0 to 255.
#
# size is the length of the cube's side.
def draw_block(x, y, color=(255, 0, 0), size=30):
    turtlehelpers.pauseDrawing()
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()

    # The right side
    t.fillcolor(blend_colors(color, (0, 0, 0)))
    t.begin_fill()
    t.forward(size)
    t.right(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(60)
    t.forward(size)
    t.end_fill()

    # The left side
    t.fillcolor(blend_colors(color, (0, 0, 0), weight1=3.0))
    t.begin_fill()
    t.right(60)
    t.forward(size)
    t.right(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.end_fill()

    # The top side
    t.fillcolor(color)
    t.begin_fill()
    t.right(180)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(60)
    t.forward(size)
    t.end_fill()

    turtlehelpers.unpauseDrawing()


##### EXERCISE 1 #####
#
# Let's draw two cubes.

draw_block(x = 50, y = -100, color = (255, 128, 64))
draw_block(x = 0, y = -200, color = (128, 16, 192))

# Move one of the cubes to directly on top of the other by changing
# the coordinates in the above function calls. The x and y define
# where cube's "lowest" vertex is located in 2D coordinates.
#
# Note that the lower cube must be painted first so that its top part
# gets covered by the second cube.
#
# Try changing the colors of the cubes.

##### EXERCISE 2 #####
#
# Add more cubes on each side of the first cube.
#
# You need to figure out the coordinates where to draw a cube so that
# it appears to be to the left or right or on the front or on the back
# of another cube. Create a function that computes the coordinates.
#
# When you have the function, you can build structures by controlling
# how cubes are placed relative to each other.
