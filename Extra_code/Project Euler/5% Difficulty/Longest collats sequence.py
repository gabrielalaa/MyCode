# My method:
# def collatz_sequence(n):
#     sequence = []
#     while n != 1:
#         sequence.append(n)
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3*n + 1
#     sequence.append(1)
#     return sequence
#
#
# def longest_collatz_sequence():
#     # Under one million 1_000_000
#     max_sequence = []
#     for i in range(999999, 1, - 1):
#         sequence = collatz_sequence(i)
#         if len(sequence) > len(max_sequence):
#             max_sequence = sequence
#     return max_sequence[0]
#
#
# # print(collatz_sequence(13))
# print(longest_collatz_sequence())


###
# Efficient method:

def collatz_sequence_length(n, memo):
    original = n
    length = 0
    while n != 1:
        if n in memo:
            memo[original] = length + memo[n]
            return memo[original]
        length += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    memo[original] = length + 1
    return memo[original]


def longest_collatz_sequence(limit):
    memo = {}
    max_length = 0
    starting_number = 0
    for i in range(limit - 1, 1, -1):
        current_length = collatz_sequence_length(i, memo)
        if current_length > max_length:
            max_length = current_length
            starting_number = i
    return starting_number


# Usage example
print(longest_collatz_sequence(1_000_000))
