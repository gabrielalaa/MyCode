# Task 1 Playing with lists
# Make a list with [ ] brackets.
my_list = [1, 2, 3]
print(f"my initial list: {my_list}")
# Append with the append() function
my_list.append(4)
print(f"my list now: {my_list}")
# Create a list with some initial elements
list = ["food", "coffee"]
print(f"a list with some initial elements: {list}")
# Create a list with N repeated elements
# Method 1
n_list = [1, 2, 3] * 4
print(f"a list with N = 4 repeated elements: {n_list}")
# Method 2
n = 5
element = "apple"
n_elements = [element for i in range(n)]
print(n_elements)
# Assign some lists to some variables. a = [1,2,3] b = 3*[‘xyz’]
a = [1, 2, 3]
b = 3 * ['xyz']
print("Assign some list to some variables: ")
print(a)
print(b)
# Try an empty list, repeated elements, initial set of elements
my_list.clear()  # an empty list
print(f"my list now: {my_list}")
# Add two lists: a + b What happens?
print(a + b)
# Try list indexing, deletion, functions from dir(my_list)
list_methods = [1, 2, 3]
print(list_methods)
print(list_methods.index(2))
del list_methods[-1]
print(list_methods)
list_methods.insert(0, 9)
print(list_methods)
last_element = list_methods.pop()
print(f"last element: {last_element}")
print(list_methods)
# tried more on python console
# Try assigning the result of a list slice to a new variable
x = ['a', 'b', 'c', 'd', 'e']
y = x[0:1]
z = x[2:5:2]
print(x)
print(y)
print(z)

#######################################################

# Task 2 Duplicates in a list
###
# Method I
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = []  # without duplicates so I need this variable for this condition
for element in a:
    if element in b and element not in common_elements:
        common_elements.append(element)
print(common_elements)
###
# Method II
a = set(a)
b = set(b)
a = a.intersection(b)
print(list(a))


#######################################################

# Task 3 List Concatenation
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# concatenate two lists index-wise
list = [list1[i] + list2[i] for i in range(len(list1))]
print(list)
# method in class
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = []
# concatenate two lists index-wise
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print(result)

#######################################################

# Task 4 Extend a list
# given list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i", "j"])
print(list1)

#######################################################

# Task 5 Factorial Digit Sum
n = int(input("Enter your number: "))
# find the factorial result
i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1
print(f"factorial is: {factorial}")
# find the number of digits
copy_factorial = factorial
digits = 0
while copy_factorial:
    digits += 1
    copy_factorial //= 10
print(f"number of digits: {digits}")
# finally the sum
i = 1
sum = 0
while i <= digits:
    sum += factorial % 10  # last digit
    factorial //= 10
    i += 1
print(f"the sum of the digits in number {n}! is: {sum}")

# updated version:
# Task 5 Factorial Digit Sum
n = int(input("Enter your number: "))
# Calculate the factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial is: {factorial}")
# Calculate the sum of the digits in the factorial
digit_sum = 0
while factorial > 0:
    digit_sum += factorial % 10  # Add the last digit
    factorial //= 10  # Remove the last digit
print(f"The sum of the digits in number {n}! is: {digit_sum}")
###
# Method III
def factorial (n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse
        return result

f = factorial(100)
sum_ = 0
while f:
    sum_ += f % 10
    f //= 10
print(sum_)

#######################################################

# Task 6 Tic Tac Toe
# Prompt user for input
input_str = input("Enter the Tic-tac-toe grid: ")
# Convert the input string to a 3x3 grid
grid = [list(input_str[i:i + 3]) for i in range(0, len(input_str), 3)]
# Initialize winner as None
winner = "None"
# Check rows and columns for winner
for i in range(3):
    if grid[i][0] == grid[i][1] == grid[i][2] != '_':
        winner = grid[i][0]
        break
    if grid[0][i] == grid[1][i] == grid[2][i] != '_':
        winner = grid[0][i]
        break
    # Check diagonals for winner
if grid[0][0] == grid[1][1] == grid[2][2] != '_':
    winner = grid[0][0]
elif grid[0][2] == grid[1][1] == grid[2][0] != '_':
    winner = grid[0][2]
# Print the winner
print("Winner:", winner)

#######################################################

# Task 7 Sudoku

sudoku = '''859612437
723854169
164379528
986147352
375268914
241593786
432981675
617425893
598736241'''

ls = sudoku.splitlines()

# Check lines
for row in ls:
    if len(list(row)) != len(set(row)):
        print("it is not a valid sudoku")

# Check columns
temp = []

for i in range(len(ls)):
    for j in range(len(ls)):
        temp.append(ls[i][j])
    if len(list(temp)) != len(set(temp)):
        print("it is not a valid sudoku")
        break
    temp = []

# Check blocks
for bg_row in range(0, 9, 3):
    for bg_col in range(0, 9, 3):
        for row in range(bg_row, bg_row + 3):
            for col in range(bg_col, bg_col + 3):
                temp.append(ls[row][col])
        if len(list(temp)) != len(set(temp)):
            print("it is not a valid sudoku")
            break
        temp = []

print("It's a valid sudoku!")

#######################################################

# Task 8 Pandigital Numbers

from itertools import permutations

# Define the pandigital numbers as all permutations of the digits 0 to 9
digits = '0123456789'
pandigital_numbers = [''.join(p) for p in permutations(digits)]

# Convert each pandigital string to an integer and calculate the sum
# Exclude numbers starting with 0 to avoid leading zero issues
sum_of_pandigitals = sum(int(number) for number in pandigital_numbers if number[0] != '0')

print(sum_of_pandigitals)

#######################################################

# Task 9 Goldbach's Other Conjecture

def isPrime (number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_twice_square(n):
    sqrt_n = (n / 2) ** 0.5
    return sqrt_n.is_integer()

# # Function to find the smallest odd composite number that cannot be written as the sum of a prime and twice a square

def goldbach_other_conjecture():
    number = 9 # Starting with the first odd composite number
    while True:
        if not isPrime(number):
            conjecture_holds = False
            # Check if the number can be expressed as the sum of a prime and twice a square
            for square in range(1, int((number // 2) ** 0.5) + 1):
                if isPrime(number - 2 * square * square):
                    conjecture_holds = True
                    break
            # If the number cannot be expressed as such, the conjecture does not hold
            if not conjecture_holds:
                return number
        number += 2 # Increment by 2 to get the next odd number

result = goldbach_other_conjecture()
print(result) # 5777

#######################################################

# Task 10 Sending secret messages (class)
smessage = "a.creenshotssf msaketw ttIw g?runkdw ptegh bromputecn pap ksoeda swoHa"
words = smessage.split(" ")
print(words)
message = []
for w in words:
    nw = w[1:len(w) - 1]  # remove the first and the last char
    nw = nw[-1] + nw[1:len(nw) - 1] + nw[0]
    message.append(nw)
message = message[::-1]
print(" ".join(message))  # list -> str

#######################################################

# try at home: to create a table
list = [
    'Joe', 'Kim',
    'Sam', 'Sue',
    'Kelly', 'Chris'
]
print(list)
# now in a table using for loops
# Determine the number of rows for the table
num_columns = 2
num_rows = len(list) // num_columns  # 6 // 2 = 3
# Print the table
for i in range(num_rows):
    for j in range(num_columns):
        # Compute the index in the list for the current column
        index = i * num_columns + j
        print(f'{list[index]:<10}', end=' ') # <:10 format specifier
        # < Indicates left alignment
        # 10 width of the formatted  filed
    print()  # New line after each row

#######################################################

# Task 11 Counting Atoms
import re
# Prompt the user for input
molecular_formula = input("Enter a molecular formula: ")
# Split the given formula in useful pieces -> list
pieces = re.findall("[A-Z][a-z]?|[0-9]+", molecular_formula)
print(pieces)
atom_count = {}  # our dictionary
i = 0
# Process each piece to count atoms
while i < len(pieces):
    element = pieces[i]
    if i + 1 < len(pieces) and pieces[i + 1].isdigit():
        count = int(pieces[i + 1])
        i += 2
    else:
        count = 1
        i += 1
    if element in atom_count:
        atom_count[element] += count
    else:
        atom_count[element] = count
    # Display the results
print("Number of atoms of each element:")
for element, count in atom_count.items():
    print(f"{element}: {count}")

#######################################################

# Task 12a
given_list = [1, 1, 2, 2, 3, 3, 4, 4, 5]
# without duplicates
print(list(set(given_list)))

# Task 12b
print(set("interesting-exercise-and-quite-useful"))
# We convert a string into a set.
# Sets in Python are unordered collections of unique elements
# Therefore, all duplicate characters are removed
# ! The original order of characters is not preserved
print("".join(set("interesting-exercise-and-quite-useful")))
# It removes all multiple occurrences of characters in the string
# Join method -> joins the elements of the set into a single string
# "" -> the separator between elements, the characters are joined without any additional characters between them

# Task 12c
first_set = {1, 2, 3, 4, 5}
second_set = {3, 4, 5, 6, 7}
print(first_set - second_set)
print(first_set.difference(second_set))

# Task 12d
print(first_set ^ second_set)
print(first_set.symmetric_difference(second_set))

#######################################################

# Task 13a Find a Rectangle
# Given a list of points like this:
L = [(10, 20), (10, 30), (10, 40), (20, 20), (20, 30), (20, 50), (30, 10)]
# this list contains tuples
# Store rectangles found
rectangles = []
# Convert the list to a set for faster lookup
point_set = set(L)
# Why a set ? Because the order doesn't matter, and we don't need repeated elements
# Iterate through each pair of points
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        e1 = L[i]
        e2 = L[j]
        # Check if e1 and e2 can be diagonal corners of a rectangle
        if e1[0] != e2[0] and e1[1] != e2[1]:
            # Identifying the Other Two Corners
            e3 = (e1[0], e2[1])
            e4 = (e2[0], e1[1])
            # Check if e3 and e4 are in the set
            if e3 in point_set and e4 in point_set:
                # Sort the points to avoid duplicates
                points = tuple(sorted([e1, e2, e3, e4]))
                if points not in rectangles:
                    rectangles.append(points)
                # Display the result
print("Rectangles found: ", rectangles)