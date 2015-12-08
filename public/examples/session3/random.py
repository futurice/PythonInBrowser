##### FILE #####
# random.py
# Let's learn how to make the computer give us random values

##### INFO #####
# If we import a thing called random, we are able to make the computer
# give us random numbers.  Random numbers are fun for creating
# computer graphics.  But let's first see how we can have different
# kinds of numbers
#
# Notice that if you press the run button several times, the computer
# draws different random numbers every time.
import random

print random.random()  # # Random float x, 0.0 <= x < 1.0

print random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0

print random.randint(1, 10)  # Integer from 1 to 10, endpoints included

print random.randrange(0, 101, 2)  # Even integer from 0 to 100

print random.choice('abcdefghij')  # Choose a random element

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print items
