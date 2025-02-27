# Write a Python function called check which takes an input parameter n and returns the total count of
# numbers below n that are both palindromic and can be written as the sum of consecutive squares.

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True


def check(n):
    c = 0
    for i in range(1, n):
        s = i ** 2
        # Add consecutive squares
        for j in range(i + 1, n):
            s += j ** 2
            if s > n:
                break  # If the sum exceeds n, no need to continue
            if is_palindrome(s):
                c += 1
    return c


print(check(1000))
# print(check(7890))
# print(check(123456))
# print(check(45623))
# print(check(98765))