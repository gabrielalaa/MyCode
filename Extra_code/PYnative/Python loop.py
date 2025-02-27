# Exercise 1

for i in range (1, 11):
    print(i)

#######################################################

# Exercise 2

row = 5
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#######################################################

# Exercise 3

number = int(input('Enter a number: '))


def all_numbers(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    return s


print('Sum is', all_numbers(number))

#######################################################

# Exercise 4

num = int(input('Enter a number: '))
for i in range(1, 11):
    print(i * num)

#######################################################

# Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i % 5 == 0 and i <= 150:
        print(i)
    else:
        if i > 500:
            break

#######################################################

# Exercise 6

num = int(input('Enter a number: '))
digits = 0
while num:
    digits += 1
    num //= 10
print(digits)

#######################################################

# Exercise 7

n = 5
k = 5
for i in range(0, n+1):
    for j in range(k-i, 0, -1):
        print(j, end=' ')
    print()

#######################################################

# Exercise 8

# Method I
list1 = [10, 20, 30, 40, 50]
list1.sort(reverse=True)
for i in list1:
    print(i)

# Method II
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

#######################################################

# Exercise 9

for i in range (-10, 0):
    print(i)

#######################################################

# Exercise 10

for i in range(5):
    print(i)
else:
    print("Done!")

#######################################################

# Exercise 11

# Method I
s = int(input('Enter a number: '))
e = int(input('Enter another number: '))


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(s, e):
    if check_prime(i):
        print(i)

# Method II
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)

#######################################################

# Exercise 12

# first two numbers
num1, num2 = 0, 1

print("Fibonacci numbers: ")
# run loop 10 times
for i in range(10):
    print(num1, end =" ")
    # add last two numbers to get next number
    num3 = num1 + num2

    # update values
    num1 = num2
    num2 = num3

#######################################################

# Exercise 13

# Method I
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))


# Method II
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

#######################################################

# Exercise 14


def inverse(number):
    string = str(number)
    return int(string[::-1])


print(inverse(76542))


#######################################################

# Exercise 15

# Method I
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0, len(my_list)):
    if i % 2 != 0:
        print(my_list[i], end=" ")

# Method II
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ")

#######################################################

# Exercise 16

input_number = 6
for i in range(1, input_number + 1):
    print(f"Current Number is : {i} and the cube is {i**3}")

#######################################################

# Exercise 17

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)

#######################################################

# Exercise 18

for i in range(6):
    for j in range(1, i + 1):
        print('*', end=' ')
    print()
k = 4
n = 4
for i in range(n + 1):
    for j in range(k - i, 0, -1):
        print('*', end=' ')
    print()