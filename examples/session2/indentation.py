# Sequences, loops

import turtle

##### INFO #####
#
# A loop can be used to repeat a block of commands several times.
#
# Below is an example of a loop syntax. range(10) tells how many times
# the command is repeated. The commands that are repeated are written
# after the for line. The repeated commands must be indented with two
# spaces.
#
# for i in range(10):
#   print i

##### EXERCISE #####

# Can you figure out what are the next values in the following
# sequence? Write down the next 4 values.
[4, 7, 10]

# The next loop computes the first 20 values of the same sequence.

number = 4
sequence = [number]

for i in range(20):
  number = number + 3
  print 'Appending number', number, 'to the sequence'
  sequence.append(number)

# The following commands are not part of the loop anymore because they
# are not indented.
  
print 'After the loop sequence is'
print sequence

# Let's draw something using the sequence we just computed. Remove the
# comment characters from the beginning of the following lines:

# t = turtle.Turtle()
# for s in sequence:
#   t.forward(s)
#   t.right(60)

# Change the sequence (the calculation in the first loop) or the angle
# (the number in the t.right(60) in the second loop) and see want
# happens.
