# Exercise 1

string = input('Enter a string: ')
new_string = string[0] + string[len(string) // 2] + string[-1]
print(new_string)

#######################################################

# Exercise 2

string = input('Enter a string: ')
new_string = string[len(string) // 2 - 1] + string[len(string) // 2] + string[len(string) // 2 + 1]
print(new_string)

#######################################################

# Exercise 3

s1 = "Ault"
s2 = "Kelly"

# Find the middle of the string
middle = len(s1) // 2

# Find the left and right parts
left = s1[:middle]
right = s1[middle:]

new = left + s2 + right
print(new)

#######################################################

# Exercise 4

s1 = "America"
s2 = "Japan"

new = s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
print(new)


#######################################################

# Exercise 5


def letters(string):
    list_l = [s for s in string if s.islower()]
    list_u = [s for s in string if s.isupper()]
    print(''.join(list_l) + ''.join(list_u))


str1 = 'PyNaTive'
letters(str1)

#######################################################

# Exercise 6

s1 = "Abc"
s2 = "Xyz"

# IF WE HAVE THE SAME LENGTH method
# s1 and s2 have the same length
length = len(s1)

# Create s3
# Reverse s2 first
s2 = s2[::-1]
s3_list = []
for i in range(length):
    s3_list.append(s1[i] + s2[i])

print(''.join(s3_list))

##########################################

# IF WE DON'T HAVE THE SAME LENGTH method
# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)


#######################################################

# Exercise 7

# Balanced

def balanced(s1, s2):
    for _ in s1:
        if _ not in s2:
            return False
    return True


s1 = input("Enter")
s2 = input("Enter")
print(balanced(s1, s2))

#######################################################

# Exercise 8

# Ignoring the case
# Make the string a list
string = input("Enter").lower()
occurrence = input("Enter the occurrence").lower()
# Method 1
print(string.count(occurrence))

# Method 2

import re

# Input string
input_string = input("Enter the string: ")

# Pattern to match 'USA' or 'usa' ignoring case, and allowing for punctuation around
pattern = r'\bUSA\b|\busa\b'

# Using re.findall to find all occurrences ignoring case, and re.IGNORECASE to ignore case
matches = re.findall(pattern, input_string, re.IGNORECASE)

# Printing the number of occurrences
print("Occurrences of 'USA':", len(matches))

#######################################################

# Exercise 9

# Sum and average of the digits present in a string

str1 = input("Enter")

# Calculate the sum
s = sum(int(c) for c in str1 if c in "0123456789")
# Calculate the length
l = 0
for element in str1:
    if element.isnumeric():
        l += 1
print(f"Sum is: {s} Average is {s / l}")


#######################################################

# Exercise 10

# Method 1
# Create a function which takes each letter
def letters(letter):
    # If the letter is already in the dictionary, add 1
    if letter in my_dict:
        my_dict[letter] += 1
    else:
        # If the letter is not in the dictionary, let it be 1
        my_dict[letter] = 1


str1 = input("Enter")

# Create an empty dictionary
my_dict = {}

for i in str1:
    letters(i)

print(my_dict)

######
# Method 2
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

#######################################################

# Exercise 11
# Method 1
str1 = input('Enter a string: ')

# Reverse the string
print(str1[::-1])

###
# Method 2
str1 = "PYnative"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)

#######################################################

# Exercise 12

str1 = input("Enter a string: ")
occurrence = input("Enter")

find = str1.rfind(occurrence)
print(f'Last occurrence of Emma starts at index {find}')

#######################################################

# Exercise 13

str1 = 'Emma-is-a-data-scientist'

# Create a list based on '-' as a separator
# str1.split('-')
for word in str1.split('-'):
    print(word)

#######################################################

# Exercise 14

# Method 1
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(f"Original string:\n {str_list}")

new_list = []
for word in str_list:
    if word:
        new_list.append(word)

print(f"New string:\n {new_list}")

###
# Method 2
# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)

#######################################################

# Exercise 15

import string

# Method 1
# Remove special symbols
str1 = input("Enter a string: ")

new = list(filter(lambda x: x not in string.punctuation, str1))

print(''.join(new))
print(' '.join(''.join(new).split()))

###
# Method 2
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

###
# Method 3
import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)

#######################################################

# Exercise 16

# Remove all characters except integers

str1 = input("Enter a string: ")

# or using .isdigit()
new = [digit for digit in str1 if digit in '0123456789']
print(''.join(new))


#######################################################

# Exercise 17

# Method 1
def find(word):
    flag1, flag2 = 0, 0
    for element in word:
        if element.isdigit():
            flag1 = 1
        elif element.isalpha():
            flag2 = 1
        else:
            return 0
    if flag1 == 1 and flag2 == 1:
        return 1


str1 = input("Enter a string: ")
str1 = str1.split()

for _ in str1:
    flag = find(_)
    if flag == 1:
        print(_)

###
# Method 2
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

#######################################################

# Exercise 18

# Replace each special symbol with #
# Method 1
import string

str1 = input("Enter a string: ")
new = ''

for i in str1:
    if i in string.punctuation:
        new += '#'
    else:
        new += i

print(new)

###
# Method 2

import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
