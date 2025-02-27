# A harmonic sequence has numbers formed by taking the reciprocals of an arithmetic sequence
# If we start with a simple arithmetic sequence like: 2, 4, 6, 8, 10, ...
# The harmonic sequence would be: 1/2, 1/4, 1/6, 1/8, 1/10, ...
def arithmetic_sequence(seq):
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


def harmonic_sequence(seq):
    # Calculate the reciprocals
    reciprocals = [1 / x for x in seq]
    # Check if the reciprocals form an arithmetic sequence
    return arithmetic_sequence(reciprocals)


s = [1/2, 1/4, 1/6, 1/8, 1/10]
print(harmonic_sequence(s))
s = [1/2, 1/4, 1/6, 1/8, 1/11]
print(harmonic_sequence(s))
