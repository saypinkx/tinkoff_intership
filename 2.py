
dictionary = {'s': 0,
              'h': 0,
              'e': 0,
              'r': 0,
              'i': 0,
              'f': 0,
              }

string = str(input())

for char in string:
    if char in dictionary:
        dictionary[char] += 1
dictionary['f'] = dictionary['f'] // 2

print(min(list(dictionary.values())))
