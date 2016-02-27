# Let's go through what we learnt last week (and something new)
# If something is unclear, don't hesitate to ask for help!

##### INFO #####
# The most important things we learnt last week were:
# 1. printing
# 2. use of variable
# 3. use of turtle for drawing

# Programming often requires looking for information from another source
# and then then applying that information to your own program.
# In practice internet is a very good source for information.
# To make it easier use last week's exercises
# as a source for information for the following exercises:


##### EXERCISES #####

##### EXERCISE 1 #####
# 1. write code that prints two separate lines
# The first line should contain the text:
# "My favorite color is 'your favorite color'"
# The second line should contain an equation
# that counts how many days are left in this month.
# HINT: December has 31 days, check the current date from your computer.
# Your printing should contain just one number: the result of the equation.

# <------ write your code here (and click 'Run' to print) ------->

##### EXERCISE 2 #####
# One day your favorite color might be green, the next day it's orange.
# Create a variable named favoriteColor and assign your favorite color as a value to it.

# <------  write the variable here ------->

# Then write a line that prints text "My favorite color is 'your favorite color'"
# But use a variable to express your favorite color this time.

# <------  write the printing code here (and click 'Run' to print) ------->

# Then as the check, change the value of the favoriteColor variable and click 'Run'
# and check that it is printing correctly, with the new favorite color.


##### EXERCISE 3 #####
# In order to be able to draw on the canvas, we need to use a turtle who draws
# To achieve that we must import the turtle and assign it to a variable.

# <------ import turtle here ------->
# like this: import turtle
# <------ assign turtle here to a variable called 'jane', remember? ------>

# Draw a simple line with the turtle that moves followingly:
#
# forward 50 pixels, turns 135 degrees right,
# forward 100 pixels, turns 135 degrees right, forward 100 pixels,
# turns 135 degrees right and goes forward 50 pixels
#
# Try to guess what kind of shape you're about to draw.

# <------ write your code here ------->

# It's possible to draw with other colors. Black is just the default color.
# Turtle's color can be changed by adding the following line before 
# the drawing code:
# jane.color("pink")

# It's also possible to use a variable to define the color for drawing.
# Replace the color changing code with a following line and click 'Run':
#
# jane.color(favoriteColor)
#
# Note that when you are using variables, you don't need quotation marks.

# Congratulations! You've just gone through the most essential things from last week
# and also learnt something new: to draw with different colors.

##### ADDITIONAL EXERCISE #####

# What would be the easiest way to complete the triangle?
# Try changing the value of 'favoriteColor' and test that it works.
# How would you draw another triangle in different direction with different color?
