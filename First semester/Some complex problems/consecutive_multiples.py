# CONSECUTIVE MULTIPLES - which shares at least a digit in common
def consecutive_multiples(n, m):
    # x must be at least a multiple of m
    x = m
    while True:
        # Create a list of the next n-1 multiples of m
        multiples = [x+i*m for i in range(n)]

        # Convert the digits of the first multiple into a set
        common_digits = set(str(multiples[0]))

        # Check if multiples share at least a digit in common with the first multiple
        for multiple in multiples[1:]:
            # Convert the digits of this multiple into a set
            multiple_digits = set(str(multiple))

            # Find the intersection of digits between the common set and the current set
            common_digits = common_digits.intersection(multiple_digits)

            # If there are no common digits, stop the loop
            if not common_digits:
                break

        # If common digits are found across all multiples, return x
        if common_digits:
            return x

        # If not, increment x to check the next potential series of multiples
        x += 1


print(consecutive_multiples(3, 5))
# n = 3
# m = 5
# x = consecutive_multiples(n, m)
# for i in range(n):
#     print(x + i * m)