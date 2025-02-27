def sum_digits(n):
    # Base case: if n is a single digit
    if n < 10:
        return n
    else:
        # Recursive case: sum the last digit (n % 10) with the sum of the digits of the quotient (n // 10)
        return n % 10 + sum_digits(n // 10)


# Test data and results
result_345 = sum_digits(345)  # Output is 12
result_45 = sum_digits(45)  # Output is 9
