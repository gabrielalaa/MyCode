from itertools import permutations

S, R = map(str, input().split())
R = int(R)

# Create a list of letters
list_of_letters = []
for letter in S:
    list_of_letters.append(letter)

# Remove the multiple letters and sort the list
# reverse=False by default
list_of_letters = list(sorted(set(list_of_letters)))

for element in (list(permutations(list_of_letters, R))):
    print(''.join(element))