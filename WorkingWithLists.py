# Working with Lists

# Looping through an entire list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# This tells Python to pull a name from the list and store it as a newly-created variable called 'magician'
# Python then repeats this until every list item "in" magicians has been actioned like this

# Other examples
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# Numbered Lists

numbers = list(range(1,6))
# This lists 1-5 (Python stops at the position you give it, so 1-5 would result in 5 being missing.
# This leads to a weird 'off-by-one' quirk on the ending number.
print(numbers)

# Even numbers
even_numbers = list(range(2,13,2))
# Odd numbers
odd_numbers = list(range(1,12,2))
print(odd_numbers)
print(even_numbers)
# The last number in that range function argument is how much Python should count upwards by until it reaches
# (or passes) the upper limit. E.g. (2,13,2) means start at 2, end at 13, and count up by 2 each time, resulting
# in 2, 4, 6, 8, 10, 12

