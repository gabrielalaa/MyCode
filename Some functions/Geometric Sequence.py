# A geometric sequence has a constant ratio between any successive sequence elements
def geometric_sequence(seq):
    # A sequence with less than 2 elements is geometric
    if len(seq) < 2:
        return True

    # Save the ratio between first 2 elements
    ratio = seq[1] / seq[0]
    for i in range(2, len(seq)):
        # If the ratio between the new element and the previous one is differenet => False
        if seq[i] / seq[i - 1] != ratio:
            return False

    return True


s = list(map(int, input().split()))
print(geometric_sequence(s))
