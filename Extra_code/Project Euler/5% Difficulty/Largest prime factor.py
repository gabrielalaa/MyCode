import math


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def prime_factors(n):
    prime_factors = []

    # Check for small factors first
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i

    # If n is still greater than 1, it must be prime
    if n > 1:
        prime_factors.append(n)

    return prime_factors[-1]


# print(prime_factors(13195))
print(prime_factors(600851475143))