numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # Sorts in ascending order
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

numbers = (3, 1, 4, 1, 5, 9, 2)
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # Original tuple remains unchanged