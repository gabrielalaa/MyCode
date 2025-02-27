# Task 1 Leap Year Identifier
year = int(input("Input year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

#########################################################################

# Task 2 Electricity Bill
electricity_units = int(input("Enter electricity units: "))
if electricity_units <= 50:
    total_bill = electricity_units * 0.50
elif electricity_units <= 150:
    total_bill = (50 * 0.50) + ((electricity_units - 50) * 0.75)
elif electricity_units <= 250:
    total_bill = (50 * 0.50) + (100 * 0.75) + ((electricity_units - 150) * 1.20)
else:
    total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((electricity_units - 250) * 1.50)
    surcharge = total_bill * 0.20
    total_bill += surcharge
print(f"Total bill= € {total_bill}")

#########################################################################

# Task 3 Max of Three
###
# Method I
a = int(input("Input number one: "))
b = int(input("Input number two: "))
c = int(input("Input number three: "))
maximum = 0
if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
elif c >= a and c >= b:
    maximum = c
print(f"The maximum is {maximum}")
###
# Method II
print(max(a, b, c))

#########################################################################

# Task 4 Make my bill
# Input
meters_of_cable = float(input("How many meters?: "))
hours_worked = float(input("How many hours?: "))
# What we know ?
cable_drum_cost = 1000
cable_drum_length = 500
additional_cable_cost_per_meter = 3
hourly_rate = 50
# Calculate using if statements
# Find the total cable cost. We have additional length ? If we have extra ...
if meters_of_cable <= cable_drum_length:
    total_cable_cost = cable_drum_cost  # standard price
else:
    additional_length = meters_of_cable - cable_drum_length  # how much do we have extra?
    total_cable_cost = cable_drum_cost + additional_length * additional_cable_cost_per_meter  # recalculate the price
# How many hours ?
if hours_worked <= 40:
    total_hours_cost = hours_worked * hourly_rate  # standard price
else:
    additional_hours = hours_worked - 40  # how many do we have extra ?
    total_hours_cost = (40 * hourly_rate) + (additional_hours * hourly_rate * 2)  # recalculate the price
# Now, we can make the bill
bill = total_hours_cost + total_cable_cost
print(f"Overall cost {bill}")

#########################################################################

# Task 5 Swap Characters
given_string = input("Your string is: ")
# length_of_your_string
# l = len(given_string)
# new_string = given_string[l-1] + ... I DON'T USE C++ ANYMORE
new_string = given_string[-1] + given_string[1:-1] + given_string[0]
print(new_string)

#########################################################################

# Task 6 Join Strings
string = input("Your string is: ")
if len(string) < 2:
    print("empty string")
else:
    new_string = string[:2] + string[-2:]
    print(new_string)

#########################################################################

# Task 7 String Middle Characters
###
# Method I
sampleStr = input("Your string is: ")
if len(sampleStr) > 7 and len(sampleStr) % 2 != 0:
    middle = len(sampleStr) // 2
    middle_three = sampleStr[middle - 1] + sampleStr[middle] + sampleStr[middle + 1]
    print(f"Middle three chars are {middle_three}")
###
# Method II
given_string = input("Enter:")
if len(given_string) % 2 != 0 and len(given_string) > 7:
    middle = len(given_string) // 2
    print(given_string[middle-1:middle+2])

#########################################################################

# Task 8 Balanced word - class
###
# Method I
# get input from the user
word = input("Enter the word: ").lower()
# is the length odd or even
if len(word) % 2 == 0:  # even; if 1 odd
    # find the left hand side and right hand side
    lhs = word[0:len(word) // 2]
    rhs = word[len(word) // 2:]
else:
    lhs = word[:len(word) // 2]
    rhs = word[len(word) // 2 + 1:]
print(f"{word} = {lhs}|{rhs}", end=" = ")
# calculate the value based on a = 1, b = 2, ...
l_val = 0
for c in lhs:
    l_val += ord(c) - 96
r_val = 0
for c in rhs:
    r_val += ord(c) - 96
# compare the values for lhs and rhs
print(f"{l_val}|{r_val}")
if l_val == r_val:
    print("Balanced word")
else:
    print("NOT balanced")
# print the result
###
# Method II
word = input("Enter:")
if len(word) % 2 == 0:
    left = word[:2]
    right = word[2:]
else:
    left = word[:2]
    right = word[3:]
l_val = 0
for char in left:
    l_val += ord(char) - 96
r_val = 0
for char in right:
    r_val += ord(char) - 96
if l_val == r_val:
    print("Balanced")
else:
    print("Unbalanced")

#########################################################################

# Task 9 Looping around
# while loop
x = 0
print(x)
while x < 99:
    x += 1
    if x % 3 == 0 or x % 7 == 0:
        continue
    print(x)
# for loop
for x in range(99):
    if x % 3 == 0 or x % 7 == 0:
        continue
    else:
        print(x, end="; ")

#########################################################################

# Task 10 Looping around
# while
start_range = int(input("Input start: "))
end_range = int(input("Input end: "))
sum = 0
while start_range != end_range:
    sum += start_range ** 2
    start_range += 1
print(sum)
# for
start_range = int(input("Enter start: "))
end_range = int(input("Enter end: "))
sum = 0
for x in range(start_range, end_range):
    sum += x ** 2
print(sum)

#########################################################################

# Task 11 Loops and Strings
word = input("Enter word: ").upper()
print(word)
# word = word.upper()
for c in word:
    count = word.count(c)  # STRING METHOD
    if count >= 2:
        print("not an isogram")
        break
else:
    print("is an isogram")

#########################################################################

# Task 12 Kaprekar Numbers
###
# Method I
number = int(input("Input your number: "))
if number < 0:
    print(f"{number} is not Kaprekar")
elif number == 1:
    print(f"{number} is Kaprekar")
else:
    square = number ** 2
    square_str = str(square)
    left = int(square_str[:len(square_str) // 2])
    right = int(square_str[len(square_str) // 2:])
    if left + right == number and right != 0:  # the low-order digits of the square must be non-zero
        print(f"{number} is Kaprekar")
    else:
        print(f"{number} is not Kaprekar")
###
# Method II - corrected version
number = int(input("Enter a number: "))
# 0 is a Kaprekar number
if number == 0:
    print(f"{number} is Kaprekar")
else:
    square = number * number
    square_str = str(square)
    for split in range(1, len(square_str)):
        left = square_str[:split]
        right = square_str[split:]

        # Convert to int, handling the case where left or right is empty
        left_num = int(left) if left else 0
        right_num = int(right) if right else 0

        # Check if the sum of parts equals the number and right part is non-zero
        if left_num + right_num == number and right_num != 0:
            print(f"{number} is Kaprekar")
            break
    else:
        print(f"{number} is not Kaprekar")

#########################################################################

# Task 13 The Steinhaus Cyclus
def sum_of_digit_squares(n):
    return sum(int(digit)**2 for digit in str(n))


number = int(input('Enter a number: '))
sequence = [sum_of_digit_squares(number)]
c1 = c2 = 0

while c1 < 2 and c2 < 2:
    number = sum_of_digit_squares(number)
    if number == 1:
        c1 += 1
    elif number == 145:
        c2 += 1
    sequence.append(number)
    # Break if we've reached 1 or 145 twice
    if c1 == 2 or c2 == 2:
        break

print("Sequence: ", ", ".join(map(str, sequence))) # a single string that is a comma-separated list of the numbers