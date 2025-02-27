def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome_product(nd):
    max_palindrome = 0

    # Start from the largest nd-digit number
    upper_limit = 10 ** nd-1
    lower_limit = 10 ** (nd - 1)

    # Iterate through all possible pairs of nd-digit numbers
    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product

    return max_palindrome


print(largest_palindrome_product(3))