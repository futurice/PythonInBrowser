# Computing with functions

import turtle
t = turtle.Turtle()

##### INFO #####
# Fucntions can be used for computing things.
#
# As an example, let's consider computing an area of a
# circle. You may remember form a math class that the area
# of a circle is computed by multiplying the radius of the
# circle by itself and by the number pi.
#
# Pi is a mathematical constant. It's approximate value is
# below:

pi = 3.14159265359

# We can compute the area of a circle with radius of 15 as
# follows:

area15 = pi * 15 * 15
t.circle(15)
print 'Area of circle with radius 15 is ' + str(area15)

# Area of a bit larger circle that has radius 22 is:

area22 = pi * 22 * 22
t.circle(22)
print 'Area of circle with radius 22 is ' + str(area22)

##### EXERCISES #####

##### EXERCISE 1 #####
# What is the area of a circle that has radius of 30?


##### EXERCISE 2 #####
# Let's define a function for computing the area of a
# circle:

def circle_area(radius):
  return pi * radius * radius

# "return" means that the function finishes execution and
# the value of the expression after the "return" is computed
# and passed out of the function back to the program that
# called the function.
#
# The circle_area function, which we just defined above,
# takes one parameter called radius. We need to specify a
# value for the parameter by writing the value in
# parenthesis after the function name like this:
# circle_area(15). In this example, the radius variable in
# the function will be 15 when the function is executed.
#
# We can use the function to compute the area of circle with
# radius 15 (again) and assign the returned value to a
# variable called area15_with_function, and the print its
# value:

area15_with_function = circle_area(15)
print 'Area of circle with radius 15 computed by a function is ' + str(area15_with_function)

# 1. Check that the value you got here is the same as the
# first value we computed in this exercise. They should be
# the same because they both are the area of a circle with
# radius 15.

# 2. Compute the area of circle with radius 22 using the
# function.

# 3. Compute the area of circle with radius 30 using the
# function.

##### ADDITIONAL EXERCISE #####
# Functions can also manipulate strings. This function
# counts the number of vowels in a text string.

def count_vowels(text):
  count = 0
  for letter in text:
    if letter.lower() in u"aeiouyöä":
      count = count + 1
  return count

# For example, the following code will count the number of
# vowels in the word "Python". Remove the comment mark from
# the line below.
#
# print 'Number of vowels in the word "Python": ' + str(count_vowels("Python"))

# 1. Can you come up the words that contain 5 vowels? What
# about 6 or even more?

# 2. Write a function that counts the number of consonants
# (letters that are not vowels). Try to come up with words
# that contain as many consonants as possible.
