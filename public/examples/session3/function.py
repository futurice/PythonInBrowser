##### FILE #####
# function.py
# Let's learn to write functions

##### INFO #####
# Sometimes one wants to repeat some commands multiple times, maybe
# with minor modifications. It is possible to avoid writing the same
# commands over and over again by introducing a function.
#
# As an example, let's consider computing an area of a circle. You may
# remember form a math class that the area of a circle is computed by
# multiplying the radius of the circle by itself and by the number pi.
#
# Pi is a mathematical constant. It's approximate value is below:

pi = 3.14159265359

# We can compute the area of a circle with radius of 2 as follows:

area2 = pi * 2 * 2
print 'Area of circle with radius 2 is ' + str(area2)

# Area of a bit larger circle that has radius 3 is:

area3 = pi * 3 * 3
print 'Area of circle with radius 3 is ' + str(area3)

##### EXERCISES #####

##### EXERCISE 1 #####
# What is the area of a circle that has radius of 10?


##### EXERCISE 2 #####
# Let's define a function for computing the area of a circle:

def circle_area(radius):
  return pi * radius * radius

# After we have defined a function, we can execute the commands that
# are part of the function's definition (the indented lines after the
# def-line) by writing the function's name. (In this example the
# function consists of only one indented line, but it is possible to
# create functions with more lines).
#
# The circle_area function takes one parameter called radius. We need
# to specify a value for the parameter by writing the value in
# parenthesis after the function name like this: circle_area(2). In
# this example, the radius variable in the function will be 2 when the
# function is executed.
#
# We can use the function to compute the area of circle with radius 2
# (again):

area2_with_function = circle_area(2)
print 'Area of circle with radius 2 computed by a function is ' + str(area2_with_function)

# 1. Check that the value you got here is the same as the first value
# we computed in this exercise. They should be the same because they
# both are the area of a circle with radius 2.

# 2. Compute the area of circle with radius 3 using the function.

# 3. Compute the area of circle with radius 10 using the function.

##### ADDITIONAL EXERCISE #####
# Let's try a different function. This function counts the number of
# vowels in a text string.

def count_vowels(text):
  count = 0
  for letter in text:
    if letter.lower() in u"aeiouyöä":
      count = count + 1
  return count

# For example, the following code will count the number of vowels in
# the word "Python". Remove the comment mark from the line below.
#
# print 'Number of vowels in the word "Python": ' + str(count_vowels("Python"))

# 1. Can you come up the words that contain 5 vowels? What about 6 or
# even more?

# 2. Write a function that counts the number of consonants (letters
# that are not vowels). Try to come up with words that contain as many
# consonants as possible.
