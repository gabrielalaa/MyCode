from math import sqrt
import threading

def primeFactors(n):
    factors = []
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # n must be odd at this point so a skip of 2 is used (i.e. i += 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    # Condition if n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


def checkPrimeFactorsInRange(x, y, l, r):
    # key: nr; value: prime_fact
    prime_dict = {}

    for num in range(x, y+1):
        if primeFactors(num):
            prime_dict[num] = primeFactors(num)

    # return prime_dict

    # Save the dictionary in the list
    with lock:
        r.append(prime_dict)

# Create a thread application that prints out the prime factors
# At least 5 threads
# Collect the result
# assume range 1 to 100
# t1: 1-20...

# Create a main program to use 5 threads
if __name__ == '__main__':
    result = []
    lock = threading.Lock()  # to prevent race condition

    # Create threads for different ranges
    threads = []
    ranges = [
        (1, 20), (21, 40), (41, 60), (61, 80), (81, 100)
    ]

    # Start all the threads
    for r in ranges:
        t = threading.Thread(target=checkPrimeFactorsInRange, args=(r[0], r[1], lock, result))
        threads.append(t)
        t.start()

    # Wait for all threads to finish (join them)
    for t in threads:
        t.join()

    # Return the result
    print(result)


# print(primeFactors(28))
# print(checkPrimeFactorsInRange(28,29))