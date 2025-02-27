# Exercise 1
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
new_l1 = []
new_l2 = []
for i in range(1, len(l1), 2):
    new_l1.append(l1[i])

# or
# odd_elements = list1[1::2]

for i in range(0, len(l2), 2):
    new_l2.append(l2[i])

print(f"{new_l1}\n{new_l2}")
print(new_l1+new_l2)

#######################################################

# Exercise 2

sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)

#######################################################

# Exercise 3

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

# The length of a single chunk is:
length = len(sample_list)
chunk_size = length // 3

start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)

    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size


###
# or

def slice_and_reverse_alternate(lst):
    if len(lst) % 3 != 0:
        return "List length is not divisible by 3."
    chunk_size = len(lst) // 3
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunk = lst[i:i + chunk_size]
        chunks.append(chunk[::-1])
    return chunks


#######################################################

# Exercise 4

# My method
# Use Counter

from collections import Counter
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(Counter(sample_list))

###
# Another method
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

#######################################################

# Exercise 5

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# Assume both lists have the same length
my_set = set()
for i in range(0, len(first_list)):
    my_set.add((first_list[i], second_list[i]))

print(my_set)

###
# or
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

#######################################################

# Exercise 6

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print(intersection)

for element in intersection:
    # if element in first_set:
    first_set.remove(element)

print(first_set)

#######################################################

# Exercise 7

first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

#######################################################

# Exercise 8

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

for v in roll_number:
    if v in sample_dict.values():
        continue
    else:
        roll_number.remove(v)

print(roll_number)

###

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

#######################################################

# Exercise 9

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

unique_speeds = list(set(speed.values()))
print(unique_speeds)

###

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

#######################################################

# Exercise 10

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_items = list(set(sample_list))
print(unique_items)

tuple_unique_items = tuple(unique_items)
print(tuple_unique_items)

m = min(sample_list)
print(m)

M = max(sample_list)
print(M)
