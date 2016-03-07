# Goal: fix turtle to find a hole in the wall

# We need to remember to import a turtle every time we want to use it.
import turtle

##### INFO #####
# Here we create a wall to the middle of the screen
# You can look at the code
# but don't worry if it looks too complicated at this point.
wall = turtle.Turtle()
wall.hideturtle()
wall.speed("fastest")
wall.penup()
wall.setx(100)
wall.sety(110)
wall.pendown()
wall.sety(-400)
wall.penup()
wall.sety(140)
wall.pendown()
wall.sety(300)
wall.penup()
wall.right(90)
wall.forward(420)
wall.setx(200)

# create a red dot
wall.dot(20, "red")

# here we create new turtle, with name Joe
joe = turtle.Turtle()

# joe is taking a stroll here
joe.right(120)
joe.forward(100)
joe.right(90)
joe.forward(50)

##### EXERCISE #####
# Hit 'Run' and see where Joe is about to go.
# What do you need to add to have Joe walk to the red dot?
# Don't touch the wall!

# add code here:
