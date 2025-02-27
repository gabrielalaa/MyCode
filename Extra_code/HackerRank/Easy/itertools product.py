# Cartesian product
from itertools import product


def tuples(a, b):
    # Transform the strings into numbers
    a = [int(number) for number in a]
    b = [int(number) for number in b]
    return product(a, b)


# Save the inputs as lists
A = input().split()
B = input().split()
# Transform the strings into numbers
# A = [int(number) for number in A]
# B = [int(number) for number in B]
# Print each tuple
print(*tuples(A, B))


###
# Using map
# Cartesian product
from itertools import product


def tuples(a, b):
    # Transform the strings into numbers
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    return product(a, b)


# Save the inputs as lists
A = input()
B = input()
# Transform the strings into numbers
# A = [int(number) for number in A]
# B = [int(number) for number in B]
# Print each tuple
print(*tuples(A, B))


###
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))