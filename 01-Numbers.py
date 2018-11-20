# String function
# If you store a number as an integer, like this:
# age = 23
# ... you will find that when you want to print it among some text strings, it produces a type error when ran.
#' To get around this, use the "str()" function to tell Python to treat an integer as a string of text, like so:

age = 23

message = "Happy " + str(age) + "rd Birthday!"
print(message)


# Python 2 produces an unexpected result in this division test

division_test = 3 / 2
print(division_test)

# The answer should be 1.5, but Python displays "1". This is because it needs explicitly telling to handle the answer as a "float" (or a number with decimal places following it)
# You can do that by making sure at least one of the input numbers in the equation is a float itself.

division_test_2 = 3.0 / 2
print(division_test_2)