# Let's learn how to make the computer give us random values

##### INFO #####
# If we import a thing called random, we are able to make the computer
# give us random numbers. Random numbers are fun for creating
# computer graphics. But let's first see how we can have different
# kinds of numbers
import random

# You can print a random decimal number between 0 and 1.
print random.random()  # # Random float x, 0.0 <= x < 1.0

# It's useful to get random integer numbers.
# This can be done by calling random's function randint.
print random.randint(1, 10)  # Integer from 1 to 10, endpoints included

# You can get also random decimal number between defined range
print random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0

# This function returns a random integer but so that it's
# divisible by the third number that is given as parameter
print random.randrange(0, 101, 2)  # Even integer from 0 to 100
print random.randrange(0, 101, 7)  # integer divisible by 7 – from 0 to 98

# You can also get a random letter from a set of strings.
print random.choice('abcdefghij')  # Choose a random element

# If you have an array of numbers,
# there's a function to re-arrange them in random order
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
print items

##### EXERCISE #####
# Click 'Run' and examine the results in the console.
# Click again and check what happens.

# Notice that if you press 'Run' several times, the computer
# draws different random numbers every time.

# Try changing the parameters of the random function calls.
# Are you able to figure out what each of the parameter numbers mean?
