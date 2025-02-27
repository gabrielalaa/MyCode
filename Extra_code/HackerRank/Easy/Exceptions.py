# Errors detected during execution are called exceptions.

# Example
# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero
# a = '1'
# b = '0'
# print (int(a) / int(b))
# ZeroDivisionError: division by zero

###

# Code
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print("Error Code:", e)

T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e1:
        print('Error Code:', e1)
    except ValueError as e2:
        print('Error Code:', e2)