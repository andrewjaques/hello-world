list = []
print(list)

# Build a list
for i in range (3,21,7):
    # list.append(i + 1)
    list.insert(0,i + 1)

# Show what the list contains
print(list)

# Create a variable named sum to use below (needs to be declared ahead of being used)
sum = 0

# Loop over the list and add all of it together
for i in range(len(list)): # the use of len(list) here allows the list to be any size and the loop will always run through all of it
    sum += list[i]

# Print outcome
print(sum)