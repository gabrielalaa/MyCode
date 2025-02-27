def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]

# Filter out only even numbers
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list to print the results
print(list(even_numbers))  # Output: [2, 4, 6]

###

numbers = [1, 2, 3, 4, 5, 6]

# Using a lambda function to filter out even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]

######################################################

# A predefined list of fruits
fruits_set = {'apple', 'banana', 'cherry', 'date', 'elderberry'}

# A mixed list of fruit and vegetable names
items = ['apple', 'broccoli', 'banana', 'carrot', 'cherry', 'date']


# Define a function that checks if an item is a fruit
def is_fruit(item):
    return item in fruits_set


# Use filter to get only fruits from the items list
filtered_fruits = filter(is_fruit, items)

# Convert the filter object to a list and print it
print(list(filtered_fruits))  # Output: ['apple', 'banana', 'cherry', 'date']
