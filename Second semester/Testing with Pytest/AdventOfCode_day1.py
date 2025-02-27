digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')

def find_numbers(line):
    # Initialize an empty list to store the numbers found in the line
    numbers = []
    # Iterate over each character in the line
    for i, c in enumerate(line):
        # Check if the character is a digit
        if c.isdigit():
            numbers.append(int(c))
            continue
        # Check if the character is the start of a word that represents a number
        for n, name in enumerate(digits):
            if line[i:].startswith(name):
                numbers.append(n)
                break

    # Ensure we have at least two numbers to sum
    if len(numbers) >= 2:
        return numbers[0] * 10 + numbers[-1]
    elif len(numbers) == 1:
        return numbers[0] * 10 + numbers[0]  # Case where only one number is found
    else:
        return 0  # No numbers found in line

def main():
    total_sum = 0
    # Open the text file and read it line by line
    try:
        with open("2.txt", "r") as file:
            for line in file:
                # For each line, call the find_numbers function and add the returned value to the total sum
                total_sum += find_numbers(line)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Print the total sum of the numbers found in the text file
    print(total_sum)

if __name__ == "__main__":
    main()