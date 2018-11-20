# Lists are made of items surrounded by square brackets

bicylces = ['trek', 'cannondale', 'redline', 'specialised', 'raleigh']

# When you print a list, by default you get the machine-readable version:
print(bicylces)
# ['trek', 'cannondale', 'redline', 'specialised', 'raleigh']
# This isn't the output you want your users to see

# To access an item from the list:
print(bicylces[0].title())
# Lists are 0-indexed, meaning they start at 0 as you count - e.g. 0, 1, 2, 3 etc. The above returns the 1st item in the list with the titlecase method applied.


# To change something in the list, access the numbered item in a similar way then replace it

bicycles[0] = "giant"

print(bicylces[0].title())