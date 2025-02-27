from math import sqrt


def calculate_divisors(num):
    if num == 1:
        return 1
    divisors = 2  # Count 1 and the number itself
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            divisors += 2  # Add both divisors from the pair
            if i == num // i:
                divisors -= 1  # Correct for a perfect square
    return divisors


def triangular_number(target_divisors):
    number = 1
    while True:
        triangle_num = number * (number + 1) // 2  # Calculate the nth triangular number
        if calculate_divisors(triangle_num) > target_divisors:  # Check divisors of the triangular number
            return triangle_num
        number += 1


# Example usage
# print(triangular_number(500))
print(triangular_number(5))