# creates an iterator that returns evenly-spaced values starting with start
# import itertools
# for i in itertools.count (10, 2):
#     print (i)

###

# creates an iterator that returns elements from all the iterables, until they are exhausted
import itertools
for i in itertools.chain ([232,3232,13], 'HAPPY', ['A', 'B', 'X']):
    print (i)
# 232
# 3232
# 13
# H
# A
# P
# P
# Y
# A
# B
# X

###

for x in itertools.product('ABCD', "1234"):
    print (x)
# ('A', '1')
# ('A', '2')
# ('A', '3')
# ('A', '4')
# ('B', '1')
# ('B', '2')
# ('B', '3')
# ('B', '4')
# ('C', '1')
# ('C', '2')
# ('C', '3')
# ('C', '4')
# ('D', '1')
# ('D', '2')
# ('D', '3')
# ('D', '4')

###

# Make an iterator that filters elements from data returning only
# those that have a corresponding element in selectors that evaluates to True
Students =['Sam1', 'Sam2', 'Sam3', 'Sam4']
High_scores = [False, False, False, True]
Top_students = itertools.compress(Students, High_scores)
print(list(Top_students))  # ['Sam4']