import json

numbers = [1, 2, 3, 10, 11, 12]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)