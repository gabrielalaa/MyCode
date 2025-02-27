def secret_number(filename):
    # Read the content from the file as a list of lines and remove the spaces \n
    with open(filename, 'r') as f:
        content = f.readlines()
    content = [c.strip() for c in content]
    s = 0
    for i in content:
        # Create a new list with our numbers from each row
        new = i.split()
        new = [int(j) for j in new]
        # Determine the minimum and the maximum using max and min
        maximum = max(new)
        minimum = min(new)
        # Calculate the difference
        difference = maximum - minimum
        # print(difference)
        # Add the difference to the sum (hidden number)
        s += difference
    return s


print(secret_number('random_ums.txt'))
# Output is 10096
# print(secret_number('example.txt'))
# Output is 18