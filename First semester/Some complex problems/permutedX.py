# Write a Python function called permutedX, which takes two numbers p and q as input and returns the
# smallest positive integer x between p and q, such that 2x, 3x, 4x, 5x, contain the same digits.

# First solution
def permutedX1(p, q):
    for i in range(p, q):
        # Convert the number to a sorted list of its digits
        list_of_digits = sorted(str(i))
        # Check if 2x, 3x, 4x, 5x are permutations of x
        if all(sorted(str(i * multiplier)) == list_of_digits for multiplier in range(2, 6)):
            return i

print(permutedX1(1, 1000000))
# permutedX1(142858, 10000000)
# permutedX1(1428571, 100000000)
# permutedX1(1429858, 100000000)
# permutedX1(14285701, 100000000)


###


# Second solution
def permutedX2(p, q):
    for i in range(p, q):
        # Write all the multipliers
        x = i
        x2 = i * 2
        x3 = i * 3
        x4 = i * 4
        x5 = i * 5
        # Check if the number and the multipliers have the same digits
        # Using a set because the order doesn't matter
        if set(str(x)) == set(str(x2)) == set(str(x3)) == set(str(x4)) == set(str(x5)):
            return i
    return None

print(permutedX2(1, 1000000))
print(permutedX2(142858, 10000000))
print(permutedX2(1428571, 100000000))
print(permutedX2(1429858, 100000000))
print(permutedX2(14285701, 100000000))