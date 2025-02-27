# Consecutive Prime Sum - longest sequence
def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def longest_prime_sum(n):
    # Generate a list of primes
    primes = [x for x in range(2, n) if isPrime(x)]
    longest_seq = 0
    prime_sum = 0

    # Find the longest sequence
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            current_sum = sum(primes[i:j])
            if current_sum >= n:
                break
            if isPrime(current_sum) and (j - i) > longest_seq:
                longest_seq = j - i
                prime_sum = current_sum
    return longest_seq, prime_sum


print(longest_prime_sum(100))
print(longest_prime_sum(1000))