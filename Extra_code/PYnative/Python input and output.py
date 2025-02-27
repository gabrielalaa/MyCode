# Exercise 1

num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

res = num1 * num2
print("Multiplication is", res)

#######################################################

# Exercise 2

print('My', 'Name', 'Is', 'James', sep='**')

#######################################################

# Exercise 3

num = 8
print('%o' % num)
print(oct(num))

#######################################################

# Exercise 4

num = 458.541315
print(round(458.541315, 2))
print('%.2f' % num)

#######################################################

# Exercise 5

numbers = []
for i in range(5):
    numbers.append(float(input("Enter: ")))
print(numbers)

#######################################################

# Exercise 6

# read the content of a file
with open('given.txt', 'r') as f:
    # as a list of lines
    lines = f.readlines()
# open a new file in writing mode
with open('output.txt', 'w') as f:
    # count the lines
    count = 0
    for line in lines:
        # skip the 5th line
        if count == 4:
            count += 1
            continue
        else:
            # write the current line
            f.write(line)
        count += 1

#######################################################

# Exercise 7

str1, str2, str3 = input("Enter three strings: ").split()
print('Name1', str1)
print('Name2', str2)
print('Name3', str3)

#######################################################

# Exercise 8

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

#######################################################

# Exercise 9
# Method I


def empty(filename):
    with open(filename) as f:
        content = f.read()
    if content:
        return True
    return False


print(empty('given.txt'))

# Method II

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

#######################################################

# Exercise 10

with open('given.txt', 'r') as f:
    lines = f.readlines()
    print(lines[3])