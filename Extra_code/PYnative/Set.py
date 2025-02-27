# Exercise 1

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

my_set = sample_set.copy()
my_set.update(sample_list)
print(my_set)
# {'Black', 'Blue', 'Orange', 'Green', 'Red', 'Yellow'}

#######################################################

# Exercise 2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.intersection(set2)
print(set3)

#######################################################

# Exercise 3

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.union(set2)
print(set3)

#######################################################

# Exercise 4

set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1 = set1.difference(set2)
print(set1)

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

#######################################################

# Exercise 5

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

#######################################################

# Exercise 6

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)
print(set3)

#######################################################

# Exercise 7

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.intersection(set2):
    print(set1.intersection(set2))
else:
    print("No element in common")

###

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))

#######################################################

# Exercise 8

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the intersection
intersection = set1.intersection(set2)

# Find the items from set2 but not set1
difference = set2.difference(set1)

# Add the elements from set2
set1.update(difference)
# Remove the common elements
set1 = {element for element in set1 if element not in intersection}

print(set1)

###

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

#######################################################

# Exercise 9


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)