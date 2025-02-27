def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


#################################################

def rfact(n):
    if n == 0:
        return 1
    else:
        return n * rfact(n - 1)


#################################################

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


#################################################

import math


def factorial(n):
    return (math.factorial(n))


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))

#################################################

import numpy

n = 5
x = numpy.prod([i for i in range(1, n + 1)])
print(x)

#################################################

# Function to find prime factors of a number
def primeFactors(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

#################################################

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
