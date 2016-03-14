# Goal: draw a triangle and learn to use a variable.

import turtle
t = turtle.Turtle()
t.shape("arrow")

##### INFO #####
# Let's draw a triangle with 150 pixels long sides.

# We store the length in to a variable. We can retrieve the
# value of the variable later in the code.

side = 150

# Let's divide the above line into components:
# 'side' is the name of a variable.
# '=' is used to assign a value to a variable.
# '150' is the value we assign to the variable.

##### EXERCISE #####
# The next code will draw a triangle. The name 'side' in the
# following will mean the same as the number 150. Click 'Run'!

t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)

# Draw a smaller triangle by changing the number to 60 on
# the line 13. Because a variable was used to draw the
# triangle, you only need to change the value in one place
# instead of in each three t.forward commands.  Click 'Run'
# again.

# Next, draw a larger triangle by changing the number on
# line 13 again.
