##### FILE #####
# start3.py
# Let's go through what we learned last week.
# If something is unclear, don't hesitate to ask for help!

##### INFO #####
# In the last session, we learned these functions:
# Goto, pendown, penup, color
# We also learned how to write a For -loop

import turtle
t = turtle.Turtle()

def leaf(x):
  if x == 0:
    return
  else:
    t.forward(x/10.0)
    t.right(10)
    leaf(x - 1)

# We have pre defined this function called leaf for you to use in your code.
# We'll also learn more about functions later in this session.

##### EXERCISES #####
# 1.
# Go to point (-200, 200) and choose a color of your choice.
# For six times draw leaf with value 102.

# 2.
# Go to point (-50, 30) and choose a color of your choice that is different
# from the one you chose before.
# For six times draw leaf with value 102.

# 3.
# Go to point (100, -100) and choose a color of your choice that is different
# from the one you chose before.
# For six times draw leaf with value 102.

# Note! You don't want to see anything else on your canvas than what is drawn in the leaf function.
# So take care to add penup and pendown when needed.


# 4.
# After drawing all these steps take a look at your code.
# Is there some steps you are repeating over and over again?
# In next exercises we learn a way to fix this!
