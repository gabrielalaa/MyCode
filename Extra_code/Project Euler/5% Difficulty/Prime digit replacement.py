import itertools
import math

# Helper function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Function to generate all primes up to a limit using Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    return primes

# Function to find the smallest prime in an 8 prime value family
def find_smallest_prime_in_family():
    limit = 1000000  # Set a reasonable limit for prime generation
    primes = sieve_of_eratosthenes(limit)
    primes_set = set(primes)  # For quick prime look-up

    for prime in primes:
        prime_str = str(prime)
        length = len(prime_str)
        # Try replacing each combination of digits
        for num_replacements in range(1, length):
            # Get all combinations of positions to replace
            for positions in itertools.combinations(range(length), num_replacements):
                prime_family = []
                # Replace the digits at 'positions' with '0' to '9'
                for digit in '0123456789':
                    new_number = list(prime_str)
                    for pos in positions:
                        new_number[pos] = digit
                    # Join list back to number
                    new_number_str = ''.join(new_number)
                    # Avoid numbers with leading zeros
                    if new_number_str[0] != '0':
                        new_number_int = int(new_number_str)
                        # Check if the new number is prime
                        if new_number_int in primes_set:
                            prime_family.append(new_number_int)
                # Check if we have a family of 8 primes
                if len(prime_family) == 8:
                    return min(prime_family)  # Return the smallest prime in the family

# Find and print the result
smallest_prime = find_smallest_prime_in_family()
print(f"The smallest prime in an 8 prime value family is: {smallest_prime}")