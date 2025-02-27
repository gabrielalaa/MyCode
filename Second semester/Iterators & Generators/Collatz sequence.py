# Collatz sequence (3n+1)
# even: n // 2
# odd: 3n + 1
# regardless of the starting number, you will always eventually reach the number one

def collatz_sequence_generator(n):
    while n != 1:
        yield n  # Yield the current number first
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n  # Finally yield 1 when the sequence reaches it

# Test the generator with the starting number 7
for value in collatz_sequence_generator(7):
    print(value)

# Alternatively, collect the sequence into a list
print(list(collatz_sequence_generator(7)))