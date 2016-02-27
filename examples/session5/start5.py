# Recap of functions
import turtle
t = turtle.Turtle()

##### EXERCISES #####

##### EXERCISE 1 #####
# Call function hello with different names.
# Call function triangle with different values of side
# Explain to yourself or to your friend what does calling a function mean

def hello(name):
  print "Hi " +  name + "!"

def triangle(side):
  for i in range(0, 3):
    t.forward(side)
    t.right(120)

##### EXERCISE 2 #####
# Fill a function called multiply.
# You can test if your function works by calling function testMultiply.

def multiply(x, y):
  #fill this part
  # you might want to return something in the end of your function and not 0
  return 0

def testMultiply():
  value1 = multiply(5, 6)
  if value1 == 30:
    print u"function works, 5 * 6 = 30"
  else:
    print "Ups! Something wrong with function."

  value2 = multiply(385, 525)
  if value2 == 202125:
    print u"function works, 385 * 525 = 202 125"
  else:
    print "Ups! Something wrong with function."

##### EXERCISE 3 #####
# Write your own function.
# Things you have to decide:
#  - name of your function
#  - does it take parameters
#  - what does it do? Does it print something, calculate something, draw something or return something?
