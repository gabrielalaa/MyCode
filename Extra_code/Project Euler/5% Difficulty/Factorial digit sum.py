# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result
#
# def digits_sum(N):
#     s = 0
#     for i in str(N):
#         s += int(i)
#     return s
#
# def main(num):
#     factorial_number = factorial(num)
#     factorial_sum = digits_sum(factorial_number)
#     return factorial_sum
#
# print(main(100))

###

from math import factorial

def main(n):
    fact = factorial(n)
    fact_list = []
    for i in str(fact):
        fact_list.append(int(i))
    return sum(fact_list)

print(main(100))