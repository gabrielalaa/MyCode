# Exercise 1

tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)
# (50, 40, 30, 20, 10)

#######################################################

# Exercise 2

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
# 20

#######################################################

# Exercise 3

tuple1 = tuple([50])
print(tuple1)

###

tuple2 = (50,)
print(tuple2)

#######################################################

# Exercise 4

# Unpack
tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a, b, c, d)

###
# or using *
# example
t = (1, 2, 3, 4, 5)
a, *b = t
print(a)
print(b)  # list

#######################################################

# Exercise 5

tuple1 = (11, 22)
tuple2 = (99, 88)

# make a copy of one of the tuple
tuple3 = tuple1

tuple1 = tuple2
tuple2 = tuple3
print(tuple1)
print(tuple2)

####

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)

#######################################################

# Exercise 6

tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:5]
###
tuple3 = tuple1[3:-1]
print(tuple2)

#######################################################

# Exercise 7

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#######################################################

# Exercise 8

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# Use sort but CONVERT INTO A LIST first
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[2]))

#######################################################

# Exercise 9

# from collections import Counter
tuple1 = (50, 10, 60, 70, 50)
count = 0
for i in tuple1:
    if i == 50:
        count = count + 1

print(count)

####

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#######################################################

# Exercise 10


def check(t):
    element1, element2 = t[0], t[1]
    if element1 != element2:
        return False
    else:
        for i in tuple1[2:]:
            if element1 == i:
                continue
            else:
                return False
    return True


tuple1 = (45, 45, 45, 45)
print(check(tuple1))