def count_numbers_generator(limit=None):
    # Start with the first number in the sequence
    current = "1"
    count = 0

    while count < limit:
        yield int(current)
        next_number = ""
        i = 0

        # Process the current number to get the next number in the sequence
        while i < len(current):
            count_char = 1
            # Count the occurrences of the same digit
            while i + 1 < len(current) and current[i] == current[i + 1]:
                count_char += 1
                i += 1
            # Append the count and the digit to form the next number
            next_number += str(count_char) + current[i]
            i += 1

        # Update current number to the next number
        current = next_number
        count += 1

# Print the first 16 numbers in the sequence
for value in count_numbers_generator(16):
    print(value)