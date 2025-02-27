# Such as 1, -2, 3, -4,...
def alternating_sequence(seq):
    for i in range(1, len(seq)):
        # Check if the actual or the previous element is zero
        if seq[i] == 0 or seq[i-1] == 0:
            return False
        # Check if consecutive signs alternate
        if (seq[i] * seq[i-1]) > 0:
            return False
    return True


print(alternating_sequence([1, -2, 3, -4]))  # True
print(alternating_sequence([1, 2, -3, 4]))  # False
print(alternating_sequence([-1, 2, -3, 0]))  # False
