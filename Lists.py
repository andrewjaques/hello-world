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

bicylces[0] = "giant"

print(bicylces[0].title())

# Add an element to the end of a list with append
bicylces.append('yamaha')
print(bicylces)

# Add an element to a specific position of a list with insert (remember that position 2 is actually third in the list because it is zero-indexed)
bicylces.insert(2,'honda')
print(bicylces)

del bicylces[1]
del bicylces[3]

print(bicylces)

# Remove a list item by knowing the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# Using pop to remove and keep a value
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Organise a list by using sort (permanently changes the list)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# To reverse sort, use the reverse=True argument on the sort function
cars.sort(reverse=True)
print(cars)

# Sort temporarily using sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru'] # resets the order of the list from earlier
print("Original order of list:")
print(cars)
print("Temporary sorting of list with sorted function:")
print(sorted(cars))
print("Original order of list should remain untouched:")
print(cars)

# Print a list in reverse order of items positioning
cars.reverse()
# Note that this doesn't go reverse alphabetically, just positioning

# Find the length of a list with len
len(cars)
# You'll find len() useful when you need to identify the number of aliens
# that still need to be shot down in a game, determine the amount of data
# you have to manage in a visualization, or figure out the number of registered
# users on a website, among other tasks.

# Exercise
# Think of 5 places in the world I want to visit
# Store locations ub a list

mustgo = ["Japan", "New Zealand", "Hawaii", "Easter Island", "Italy"]

# Print the list normally
print(mustgo)
# Print the list alphabetically without modifying the original
print(sorted(mustgo))
# Show that the list is unchanged
print(mustgo)
# Show it in reverse-list order
mustgo.reverse()
print(mustgo)
# Sort alphabetically permanently
mustgo.sort()
print(mustgo)
# Make it reverse-alphabetical
mustgo.sort(reverse=True)
print(mustgo)


# Avoiding index errors
# If I ask for print(mustgo[5]), expecting the last item in the list, I'll get an index error
# This is because lists positions start at 0.
# An alternative way to get the last item in a list is to use:
print(mustgo[-1])
# 0, 1, 2, 3, 4 -- imagine -1 as moving like the ship in Asteroids; if you go off the left edge of the screen you reappear on the right

