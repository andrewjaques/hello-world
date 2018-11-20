from random import random

list = []
for i in range(5):
    list.append(random())

print(list)


# Lottery numbers

from random import randint

def lottery_ticket(range_start,range_end,guesses):
    # Check the user inputs are sensible
    if ((range_end - range_start) + 1) < guesses:
        return "Your start and end numbers give insufficient range for the number of unique guesses you want"
    elif range_start > range_end:
        return "range_start argument is larger than range_end argument, cannot create lottery ticket"
    else:
        ticket = []
        while len(ticket) != guesses:
            # print("Finding lottery number #", (len(ticket)+1), "...", sep="") # Optional progress printing
            new_number = randint(range_start,range_end)
            if new_number not in ticket:
                ticket.append(new_number)
        return sorted(ticket)

print(lottery_ticket(1,49,6))

# Change history:
# If you specify more numbers than there actually are in the range, it gets stuck in an endless loop!
# Added a check to ensure this doesn't happen
# Converted variable names to use underscores, not camelCase, to better comply with PEP8
