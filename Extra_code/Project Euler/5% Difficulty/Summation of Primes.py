import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_primes():
    num = 1
    s = 0
    while num < 2_000_000:
        num += 1
        if is_prime(num):
            s += num

    return s


print(sum_of_primes())


###


# More efficient
def sum_of_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    return sum(i for i in range(limit) if sieve[i])


# Find the sum of all primes below two million
result = sum_of_primes(2_000_000)
print(result)

