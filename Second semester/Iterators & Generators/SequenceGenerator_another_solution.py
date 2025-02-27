def SequenceGenerator(limit=None):
    # Infinite repeating sequence of digits
    digits = [1, 2, 3, 4, 3, 2, 1]
    n = 1  # Starting position
    index = 0  # Index in the digits list

    while limit is None or n <= limit:
        current_sum = 0
        current_number = ''

        # Form the number until the sum equals n
        while current_sum < n:
            current_number += str(digits[index])
            current_sum += digits[index]
            index = (index + 1) % len(digits)  # Move to the next digit, loop back if needed

        if current_sum == n:
            yield int(current_number)

        n += 1


# Example Usage:

# Variant 1: Generate 10 numbers in the sequence -  this is not working
# gen = SequenceGenerator(10)
# for x in range(10):
#     print(next(gen))

# Variant 2: Infinite generator until stopped
gen = SequenceGenerator()
for i, x in zip(range(10), gen):
    print(x)