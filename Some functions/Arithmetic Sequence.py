def arithmetic_sequence(seq):
    # An arithmetic sequence has a constant difference between any successive elements

    # Check the difference between the first inputs
    x = seq[0]
    y = seq[1]
    z = seq[2]
    d1 = y - x
    d2 = z - y
    if d1 != d2:
        return False
    else:
        # Continue checking the next ones
        for i in seq[3:]:
            d = i - z
            z = i
            if d != d1:
                return False
    return True


s = list(map(int, input().split()))
print(arithmetic_sequence(s))


###################################################

# An arithmetic sequence has a constant difference between any successive elements
def arithmetic_sequence_optimized(seq):
    # A sequence with less than 2 elements is arithmetic
    if len(seq) < 2:
        return True

    # Save the difference between first 2 numbers
    difference = seq[1] - seq[0]
    for i in range(2, len(seq)):
        # If the difference between the new element and the previous element is different => False
        if seq[i] - seq[i-1] != difference:
            return False
    return True


s = list(map(int, input().split()))
print(arithmetic_sequence_optimized(s))
