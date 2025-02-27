# Exercise 1

list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

###

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#######################################################

# Exercise 2

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# I assume both lists have the same length

list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

print(list3)

###

list4 = [i + j for i, j in zip(list1, list2)]
print(list4)

#######################################################

# Exercise 3

numbers = [1, 2, 3, 4, 5, 6, 7]
square = [i**2 for i in numbers]
print(square)

#######################################################

# Exercise 4

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []
for i in list1:
    for j in list2:
        list3.append(i+j)

print(list3)

###

res = [x + y for x in list1 for y in list2]
print(res)

#######################################################

# Exercise 5

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Reverse the second list
list2.reverse()

# I assume both lists have the same length
for i in range(len(list1)):
    print(f"{list1[i]} {list2[i]}")

###

for x, y in zip(list1, list2[::-1]):
    print(x, y)

#######################################################

# Exercise 6

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = [i for i in list1 if i]
print(list1)

###

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

#######################################################

# Exercise 7

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

#######################################################

# Exercise 8

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

#######################################################

# Exercise 9

list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break

print(list1)

###

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)

#######################################################

# Exercise 10

list1 = [5, 20, 15, 20, 25, 50, 20]

list1 = [i for i in list1 if i != 20]
print(list1)

###

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)