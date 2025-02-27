import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find_prime(target_count):
    count_prime = 0
    number = 1
    while count_prime < target_count:
        number += 1
        if is_prime(number):
            count_prime += 1

    return number


print(find_prime(10001))