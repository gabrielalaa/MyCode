# Define a tuple of word representations of numbers 0 to 9
digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')


# Define a function that takes a line of text and returns the sum of the first and last number found in the line
def findNumbers(line):
    # Initialize an empty list to store the numbers found in the line
    numbers = []
    # Iterate over each character in the line
    for i, c in enumerate(line):
        # print(i, c, end="\n")
        # If the character is a digit, convert it to an integer and add it to the numbers list
        if c.isdigit():
            numbers.append(int(c))
            continue
        # If the character is not a digit, check if it is the start of a word that represents a number
        for n, name in enumerate(digits):
            # print(n, name, end=" ")
            # If it is, add the corresponding number to the numbers list
            if line[i:].startswith(name):
                numbers.append(n)
                break
    # Return the sum of the first and last number found in the line
    return numbers[0] * 10 + numbers[-1]


# Initialize a variable to store the total sum of the numbers found in the text file
sum = 0
# Open the text file and read it line by line
with open("2.txt", "r") as file:
    for line in file:
        # For each line, call the findNumbers function and add the returned value to the total sum
        sum += findNumbers(line)

# Print the total sum of the numbers found in the text file
print(sum)