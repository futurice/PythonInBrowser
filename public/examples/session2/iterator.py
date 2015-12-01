##### FILE #####
# iterator.py
# For loop as an iterator

##### INFO #####
# A for loop is an iterator.
# It's a very handy tool for repeating patterns of code.
# The basic idea is that you specify a range
# and then the iterator repeats as many times as you specify.

##### EXERCISE #####
# Let's build a simple iterator that prints out first numbers
# and then in the second phase text.
# First let's define the range as a variable that has a value 10
myRange = 10

# Here's how an iterator loop is built:
# You start with the word 'for'
# Then specify the name of the iterator.
# It's common to use 'i' as a name for an iterator.
# Then specify the range (how many times the pattern should be repeated)
# and then end the for loop with a colon ':'

for i in range(myRange):
	print i

# Click 'Run' and see what happens.

# The for loop prints out the values of 'i'.
# For loop works in a way that the value of the iterator
# increases by one after every iteration.
# In programming, numbers usually start from 0.
# So, a range with length of 10 has 10 values: from 0 to 9.
# And those are the numbers that are printed.

# Let's make the printing a bit clearer.
# Change the code inside the for loop to be the following:
# print "The value of the iterator is now: " + str(i)

# Click 'Run'.
# If you have an error, remember that correct indentations are important in Python.

# For loop prints text 'The value of the iterator is now: ' in every iteration.
# and then the value of i added to that text.
# Why is 'str(i)' and not just 'i'?
# It's because of different data types.
# The iterator of a for loop is an integer whereas text is presented as string.
# In order to be able to combine text with numbers,
# we need to convert the number (in this case integer) into string.
# This can be done with code 'str(number)'.

# After converting the text, we have two strings
# and those can be combined using a '+'.

# This all will become clearer when we deal more with code and programming.
# So, if this all seems a bit confusing, don't worry!
