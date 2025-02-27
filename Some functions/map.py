def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

# Apply the square function to each item of the numbers list
squared_numbers = map(square, numbers)

# Convert the map object to a list to print the results
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


####

numbers = [1, 2, 3, 4, 5]

# Using a lambda function to square each number
squared_numbers = map(lambda x: x**2, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
