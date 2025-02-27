# def smallest_multiple(lower_nr, upper_nr):
#     nr = 0
#     flag = True
#     while flag:
#         nr += 2
#         if all(nr % x == 0 for x in range(lower_nr, upper_nr+1)):
#             flag = False
#     return nr
#
#
# print(smallest_multiple(1, 20))

import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def smallest_multiple(lower_nr, upper_nr):
    result = 1
    for number in range(lower_nr, upper_nr + 1):
        result = lcm(result, number)
    return result


print(smallest_multiple(1, 10))  # Output: 2520
print(smallest_multiple(1, 20))  # Output: 232792560
